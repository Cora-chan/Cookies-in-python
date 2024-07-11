from django.core.management.base import BaseCommand
from balls.models import Report


class Command(BaseCommand):
    help = "Generate Report"

    def handle(self, *args, **options):
        for report in Report.objects.all(): 
            self.stdout.write(
                self.style.SUCCESS(f'User {report.user} has seen the {report.color} color for {report.count} times.')
            )