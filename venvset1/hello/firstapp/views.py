from django.http import HttpResponse


def GET(request):
    street = request.GET.get("street", " ")
    city = request.GET.get("city", " ")
    output = "<h2>Ikea на {0}  в городе: {1}</h2>".format(street, city)
    return HttpResponse(output)

def POST(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Tom")
    output = "<h2>User</h2><h3>id: {0}  name: {1}</h3>".format(id, name)
    return HttpResponse(output)