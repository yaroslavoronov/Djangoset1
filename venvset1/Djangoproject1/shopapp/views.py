from .models import*
import datetime
import json
from django.http import HttpResponse, JsonResponse


def find_city(request):
    citys = City.objects.all().select_related()
    serializer = CitySerializer(citys, many=True)
    return JsonResponse(serializer.data, safe=False)


def find_shop(request):
    street = request.GET.get("street", -1)
    city = request.GET.get("city", -1)
    mopen = request.GET.get("open", -1)
    tym = datetime.datetime.now().time()
    shops = Shop.objects.all().select_related()

    for shop in shops:
        if shop.time_close > tym:
            if tym > shop.time_open:
                shop.open = 1
                shop.save()
            else:
                shop.open = 0
                shop.save()
        else:
            shop.open = 0
            shop.save()
    if city != -1:
        shops = shops.filter(city_id=city)
    if street != -1:
        shops = shops.filter(street_id=street)
    if mopen != -1:
        shops = shops.filter(open=mopen)

    serializer = ShopSerializer(shops, many=True)
    return JsonResponse(serializer.data, safe=False)


def find_street(request, city_ids):
    streets = Street.objects.filter(city_id=city_ids)
    serializer = StreetSerializer(streets, many=True)
    return JsonResponse(serializer.data, safe=False)


def find_street_all(request):
    streets = Street.objects.all().select_related()
    serializer = StreetSerializer(streets, many=True)
    return JsonResponse(serializer.data, safe=False)


def create_shop(request, name, city_id, street_id, building, time_open, time_close):
    city_cl = '{"name":"Mosk"}'
    street_cl = '{"name":"Th",' \
                '"city_id":1}'
    # парсинг x:
    c = json.loads(city_cl)
    s = json.loads(street_cl)
    # результатом будет словарь Python:
    City.objects.create(name=c["name"])
    Street.objects.create(name=s["name"], city_id=s["city_id"])
    Shop.objects.create(name=name, city_id=city_id, street_id=street_id, building=building,
                        time_open=time_open, time_close=time_close, open=-1)
    new_shop = Shop.objects.last()
    serializer = CreateShopSerializer(new_shop)
    return JsonResponse(serializer.data, safe=False)

