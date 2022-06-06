from rest_framework import serializers

from .models import EmailSending


class EmailSendingSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmailSending
        fields = ('recipient', 'referral_link')
