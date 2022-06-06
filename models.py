import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class MonestroUser(AbstractUser):
    pass


class EmailSending(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recipient = models.EmailField()
    referral_link = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
