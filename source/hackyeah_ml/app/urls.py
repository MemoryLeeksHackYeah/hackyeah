from django.urls import path
from . import views

urlpatterns = [
    #Main paths
    path('', views.index, name='index'),

    #Subtabs
    path('fleet', views.fleet, name="fleet"),

    path('weight', views.weight, name='weight'),
    path('remote_hubs_map', views.remote_hubs_map, name='remote_hubs_map'),
    path('show_route_for_waste_type_name/<str:waste_type_name>/', views.show_route_for_waste_type_name, name='show_route_for_waste_type_name')
]