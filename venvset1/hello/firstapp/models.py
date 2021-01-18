from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30)


class Street(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)


class Shop(models.Model):
    name = models.CharField(max_length=20)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    building = models.IntegerField()
