"""
usage: ./manage.py example core
"""

from django.core.management.base import BaseCommand

def say_something_funny():
    return 'Une fois stais un gars...'


class Command(BaseCommand):
    """Entry point for the Django command."""
    help = "Describe what the command does"

    def add_arguments(self, parser):
        parser.add_argument("dummy", type=str)

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS(
                say_something_funny()
            )
        )