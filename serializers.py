from rest_framework import serializers

from .models import MonestroUser, EmailSending


class MonestroUserSerializer(serializers.ModelSerializer):
    sendings = serializers.IntegerField()

    class Meta:
        model = MonestroUser
        fields = ('first_name', 'last_name', 'email', 'sendings')


class EmailSendingSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmailSending
        fields = ('recipient', 'referral_link')
