from django.db import models


# Create your models here.

class catshop(models.Model):
    name = models.CharField(max_length=21)
    price = models.IntegerField()
    breed = models.CharField(max_length=21)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
