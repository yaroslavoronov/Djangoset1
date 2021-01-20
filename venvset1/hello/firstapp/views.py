from django.shortcuts import render
from django.http import HttpResponse
from .models import*
import datetime
import json
from rest_framework import status
from rest_framework.response import Response

def GET_CITY(request):
    citys = City.objects.all().select_related()
    return render(request, "city.html", {"citys": citys})



def GET_SHOP(request):
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

    return render(request, "index.html", {"shops": shops})


def GET_STREET(request, city_ids):
    streets = Street.objects.filter(city_id=city_ids)
    return render(request, "street.html", {"streets": streets})


def GET_STREET_ALL(request):
    streets = Street.objects.all().select_related()
    return render(request, "street.html", {"streets": streets})


def POST(request):
    city_cl = '{"name":"Omsk"}'
    shop_cl = '{"name":"Magnit",' \
              '"city_id":10,' \
              '"street_id":11,' \
              '"building":13,' \
              '"time_open":"17:00",' \
              '"time_close":"07:00",' \
              '"open":"-1"}'
    street_cl = '{"name":"Tsentr",' \
                '"city_id":10}'
    # парсинг x:
    c = json.loads(city_cl)
    s = json.loads(shop_cl)
    str = json.loads(street_cl)
    # результатом будет словарь Python:
    City.objects.create(name=c["name"])
    Street.objects.create(name=str["name"], city_id=str["city_id"])
    Shop.objects.create(name=s["name"], city_id=s["city_id"], street_id=s["street_id"], building=s["building"], time_open=s["time_open"], time_close=s["time_close"], open=s["open"])
    new_city = City.objects.last()
    new_street = Street.objects.last()
    new_shop = Shop.objects.last()
    output = "<h2>id созданного города: {0} id созданного магазина: {1} id созданной улицы: {2}</h2>".format(new_city.id, new_shop.id, new_street.id)
    return HttpResponse(output)


