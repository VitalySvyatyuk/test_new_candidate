from datetime import timedelta

from django.core.mail import send_mail
from django.db.models import Count, Subquery
from django.db.models.expressions import OuterRef
from django.template.loader import render_to_string
from django.utils import timezone

from monestro_core.worker_backoffice import worker

from .models import MonestroUser, EmailSending
from .serializers import EmailSendingSerializer


@worker.task(name="referrals.repeat_invite", ignore_result=False)
def repeat_invite():
    """
    The user can send an invitation email with a referral_link to any email that is not registered in the system.
    Such sending is saved as EmailSending object. User cannot send more than 1 email to the same address by hands.
    Only this periodic task can send a second, repeated email in 7 days.
    This periodic task runs every day at 6:00.
    """

    count = EmailSending.objects \
        .filter(recipient=Outer('recipient')) \
        .values('recipient') \
        .annotate(recipient_count=Count('pk')) \
        .values_list('recipient_count', flat=True)

    registered_emails = MonestroUser.objects.values_list('email', flat=True)

    sendings = EmailSending.objects \
        .annotate(count=Subquery(count)) \
        .filter(count=1, created_at__date=(timezone.now() + timedelta(days=7)).date()) \
        .exclude(recipient=registered_emails)

    for sending in sendings:
        html_message = render_to_string('invite.html', {'referral_link': sending.id})

        try:
            send_mail(
                subject='Invitation to Monestro',
                from_email='Monestro <info@monestro.com>',
                message='',
                recipient_list=[sending.recipient, ],
                html_message=html_message,
                fail_silently=False,
            )
            serializer = EmailSendingSerializer(data=sending.__dict__)
            serializer.save()
    except Exception:
        continue
