from django.db import models

# Create your models here.

# For category table
class Category(models.Model):
    name = models.CharField(max_length=128, default="")
    def __str__(self):
        return self.name

# State table
class State(models.Model):
    name = models.CharField(max_length=128, default="")
    def __str__(self):
        return self.name

# Region table
class Region(models.Model):
    name = models.CharField(max_length=128, default="")
    def __str__(self):
        return self.name

# Iso table
class ISO(models.Model):
    name = models.CharField(max_length=128, default="")
    def __str__(self):
        return self.name

# The site table
class Site(models.Model):
    name = models.CharField(max_length=300)
    year = models.IntegerField(null=True)
    lattitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    descreption = models.TextField(null=True)
    justification = models.TextField(null=True)
    area_hectares = models.FloatField(null=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)
    region = models.ForeignKey("Region", on_delete=models.CASCADE, null=True)
    iso = models.ForeignKey("ISO", on_delete=models.CASCADE, null=True)
    state = models.ForeignKey("State", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
