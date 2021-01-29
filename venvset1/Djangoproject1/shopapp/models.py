from django.db import models
from rest_framework import serializers


class City(models.Model):
    name = models.CharField(max_length=30)


class Street(models.Model):
    city = models.ForeignKey(City, related_name='city_id', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)


class Shop(models.Model):
    name = models.CharField(max_length=20)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    building = models.IntegerField()
    time_open = models.TimeField()
    time_close = models.TimeField()
    open = models.IntegerField()


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ['id', 'name']


class StreetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Street
        fields = ['name', 'city']


class StreetSerializer_to_city(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Street
        fields = ['name', 'city']


class ShopSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    street = StreetSerializer_to_city()

    class Meta:
        model = Shop
        fields = ['name', 'city', 'street', 'building', 'time_open', 'time_close', 'open']


class CreateShopSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    class Meta:
        model = Shop
        fields = ['new_shop']


