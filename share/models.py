# share/models.py
from django.db import models
from django.utils import timezone
import datetime

class SharedText(models.Model):
    text = models.TextField()
    code = models.CharField(max_length=4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return timezone.now() > self.created_at + datetime.timedelta(minutes=15)

    def __str__(self):
        return self.code
