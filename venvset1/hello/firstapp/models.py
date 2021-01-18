from django.db import models


class City(models.Model):
    name = models.CharField(max_length=20)


class Shop(models.Model):
    name = models.CharField(max_length=20)
    idCity = models.IntegerField()
    idStreet = models.IntegerField()
    building = models.IntegerField()


class Street(models.Model):
    name = models.IntegerField()
    idCity = models.IntegerField()