import csv
import os
from django.core.management.base import BaseCommand
from postafacil.models import Client, City
from datetime import datetime


class Command(BaseCommand):
    help = "Import clients from CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs["csv_file"]
        csv_file_path = os.path.join("postafacil", "data", csv_file)

        try:
            with open(csv_file_path, "r") as file:
                reader = csv.DictReader(file)
                clients = []

                for row in reader:
                    date_of_birth_str = row["date_of_birth"].strip()
                    date_of_birth = datetime.strptime(
                        date_of_birth_str, "%Y-%m-%d"
                    ).date()
                    client = Client(
                        name=row["name"],
                        email=row["email"],
                        password=row["password"],
                        date_of_birth=date_of_birth,
                        city=City.objects.get(name=row["city_id"]),
                        gender=row["gender"],
                        is_active=row["is_active"],
                        phone=row["phone"],
                    )
                    clients.append(client)

                Client.objects.bulk_create(clients)
                self.stdout.write(self.style.SUCCESS("Clientes importados com sucesso"))

        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR(f"Arquivo não encontrado: {csv_file_path}")
            )
