from django.db import models
from .city import City


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    cpf = models.CharField(max_length=14)
    date_of_birth = models.DateField()
    cep = models.CharField(max_length=9)
    street = models.CharField(max_length=255)
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, related_name="clients"
    )
    gender = models.CharField(
        max_length=10,
        choices=[("M", "Masculino"), ("F", "Feminino"), ("O", "Outro")],
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(default=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name
