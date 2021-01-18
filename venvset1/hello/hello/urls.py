from django.urls import path
from firstapp import views

urlpatterns = [
    path('GET/shop/', views.GET),
    path('POST/', views.POST),
]