from django.urls import path
from shopapp import views

urlpatterns = [
    path('GET/city/', views.find_city),
    path('GET/shop/', views.find_shop),
    path('POST/<str:name>/<str:city_id>/<str:street_id>/<str:building>/<str:time_open>'
         '/<str:time_close>', views.create_shop),
    path('GET/city/<int:city_ids>/street/', views.find_street),
    path('GET/city//street/', views.find_street_all),
]