import csv
import os
from django.core.management.base import BaseCommand
from postafacil.models import City


class Command(BaseCommand):
    help = "Import cities from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs["csv_file"]

        csv_file_path = os.path.join("postafacil", "data", csv_file)

        try:
            with open(csv_file_path, "r") as file:
                reader = csv.DictReader(file)
                cities = []

                for row in reader:
                    city = City(name=row["name"], state=row["state"])
                    cities.append(city)
                cities.sort(key=lambda x: x.name)

                City.objects.bulk_create(cities)

            self.stdout.write(self.style.SUCCESS("Cidades importadas com sucesso"))

        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR(f"Arquivo não encontrado: {csv_file_path}")
            )
