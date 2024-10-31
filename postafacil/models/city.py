from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name} {self.state}"
