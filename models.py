import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class MonestroUser(AbstractUser):
    
    @property
    def sendings(self):
        return self.sendings.count()


class EmailSending(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recipient = models.EmailField()
    referral_link = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    user = models.ForeignKey(MonestroUser, on_delete=models.CASCADE, related_name='sendings')
