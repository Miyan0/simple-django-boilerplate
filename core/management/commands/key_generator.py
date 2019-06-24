"""
usage: ./manage.py key_generator
"""
import random
from string import ascii_letters, digits

from django.core.management.base import BaseCommand


def generate_key():
    special_chars = "!@#$%^&*(-_=+)"

    return "".join(
        random.SystemRandom().choice(ascii_letters + digits + special_chars)
        for i in range(50)
    )


class Command(BaseCommand):
    """Entry point for the Django command."""


    help = "Generates a random 50 characters string for secret key usage"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(generate_key()))

