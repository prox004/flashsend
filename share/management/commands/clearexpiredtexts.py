# share/management/commands/clearexpiredtexts.py
from django.core.management.base import BaseCommand
from share.models import SharedText
from django.utils import timezone
import datetime

class Command(BaseCommand):
    help = 'Deletes expired texts'

    def handle(self, *args, **kwargs):
        expiration_time = timezone.now() - datetime.timedelta(minutes=15)
        SharedText.objects.filter(created_at__lt=expiration_time).delete()
