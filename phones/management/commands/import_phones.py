import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phones.models import Phone



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                phone = Phone.objects.create(
                    name=row['name'],
                    price=row['price'],
                    image=row['image'],
                    release_date=row['release_date'],
                    lte_exists=row['lte_exists'],
                    slug=slugify(row['name'])
                )
                phone.save()