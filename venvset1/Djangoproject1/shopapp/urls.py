from django.urls import path
from shopapp import views

urlpatterns = [
    path('receive/city/', views.find_city),
    path('receive/shop/', views.find_shop),
    path('create/<str:name>/<str:city_id>/<str:street_id>/<str:building>/<str:time_open>'
         '/<str:time_close>', views.create_shop),
    path('receive/city/<int:city_ids>/street/', views.find_street),
    path('receive/city//street/', views.find_street_all),
]