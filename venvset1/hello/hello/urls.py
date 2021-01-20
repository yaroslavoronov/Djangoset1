from django.urls import path
from firstapp import views

urlpatterns = [
    path('GET/city/', views.GET_CITY),
    path('GET/shop/', views.GET_SHOP),
    path('POST/shop', views.POST),
    path('GET/city/<int:city_ids>/street/', views.GET_STREET),
    path('GET/city//street/', views.GET_STREET_ALL),
]