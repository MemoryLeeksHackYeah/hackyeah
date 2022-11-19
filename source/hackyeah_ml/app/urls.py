from django.urls import path

from . import views

urlpatterns = [
    #Main paths
    path('', views.index, name='index'),

    #Subtabs
    path('fleet', views.fleet, name="fleet")

    path('maps', views.maps, name='maps'),
    path('weight', views.weight, name='weight'),
]