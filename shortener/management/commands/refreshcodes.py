from django.core.management.base import BaseCommand, CommandError

from shortener.models import conutURL


class Command(BaseCommand):
    help = 'Refrehes all conutURL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return conutURL.objects.refresh_shortcodes(items=options['items'])