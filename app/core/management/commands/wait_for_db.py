import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        """Handle the command"""
        self.stdout.write('Veritabanı bekleniyor...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Veritabanı mevcut değil, 1 saniye bekliyor...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Veritabanı mevcut!'))
