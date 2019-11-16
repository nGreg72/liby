from django.core.management.base import BaseCommand
from root.root.apps.exchange.models import SpZakup


class Command(BaseCommand):
    def handle(self, *args, **options):
        for c in SpZakup.objects.using('new').all():
            print(c.title)