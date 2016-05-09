from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Deletes old job logs.'

    def add_arguments(self, parser):
        parser.add_argument('unit', choices=['weeks', 'days', 'hours', 'minutes'])
        parser.add_argument('interval', type=int)

    def handle(self, **options):
        from chronograph.models import Log
        from datetime import datetime, timedelta
        kwargs = {options['unit']: options['interval']}
        time_ago = datetime.now() - timedelta(**kwargs)
        Log.objects.filter(run_date__lte=time_ago).delete()
