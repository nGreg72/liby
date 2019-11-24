#!/usr/bin/env python3
import sys
import os

from django.core.management.base import BaseCommand
from liby.root.root.apps.exchange.models import SpZakup
# from .models import SpZakup

class Command(BaseCommand):
    def handle(self, *args, **options):
        for c in SpZakup.objects.using('new').all():
            print(c.title)

print( globals())