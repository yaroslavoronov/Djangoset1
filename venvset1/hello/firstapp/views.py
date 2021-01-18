from django.shortcuts import render
from django.http import HttpResponse
from .models import*

def GET_CITY(request):
    citys = City.objects.all()
    return render(request, "city.html", {"citys": citys})


def GET_SHOP(request):
    shops = Shop.objects.all().select_related()
    return render(request, "index.html", {"shops": shops})

def POST(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Tom")
    output = "<h2>User</h2><h3>id: {0}  name: {1}</h3>".format(id, name)
    return HttpResponse(output)


# заполнение бд
def create(request):
    City.objects.create(name='Moskwa')
    Street.objects.create(name='Uls', city_id='1')
    Street.objects.create(name='Ulsk', city_id='1')
    Shop.objects.create(name="IKEA", city_id=1, street_id=1, building=12)
    Shop.objects.create(name="Lenta", city_id=1, street_id=2, building=11)

    return HttpResponse("/")


