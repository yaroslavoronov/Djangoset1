from django.test import TestCase
from .models import*
import datetime


class ModelTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        City.objects.create(name="namecity")
        Street.objects.create(name="namestreet", city_id="1")
        Shop.objects.create(id=1, name="shopname", city_id=1, street_id=1, building=11,
                            time_open="16:00", time_close="08:00", open=-1)
        pass

    def test_city(self):
        city = City.objects.get(id=1)
        field_label = city.name
        self.assertEquals(field_label, 'namecity')
        pass

    def test_street(self):
        street = Street.objects.get(id=1)
        name = street.name
        city_id = street.city_id
        self.assertEquals(name, 'namestreet')
        self.assertEquals(city_id, 1)
        pass

    def test_shop(self):
        shop = Shop.objects.get(id=1)
        name = shop.name
        city_id = shop.city_id
        street_id = shop.street_id
        building = shop.building
        time_open = shop.time_open
        time_close = shop.time_close
        open = shop.open
        self.assertEquals(name, 'shopname')
        self.assertEquals(city_id, 1)
        self.assertEquals(street_id, 1)
        self.assertEquals(building, 11)
        self.assertEquals(time_open,  datetime.time(16, 0))
        self.assertEquals(time_close,  datetime.time(8, 0))
        self.assertEquals(open, -1)
        pass
