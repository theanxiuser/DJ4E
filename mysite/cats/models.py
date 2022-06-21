from django.db import models

# Create your models here.

# breed class
class Breed(models.Model):
    name = models.CharField(max_length=200)

# cat class
class Cat(models.Model):
    nickname = models.CharField(max_length=200)
    weight = models.FloatField()
    breed = models.ForeignKey("Breed", on_delete=models.CASCADE, null=False)