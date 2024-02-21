"""
Django command to wait for the database to be available
"""

import time

from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Check if the Database is up. Use before running application.'
    """Django command to wait for database"""

    def handle(self, *args, **options):
        """Entry point for command"""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError) as e:
                self.stdout.write(
                    self.style.ERROR(
                        f'Error in connecting to database: {str(e)}'
                        )
                    )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
