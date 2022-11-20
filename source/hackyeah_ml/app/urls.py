from django.urls import path
from . import views

urlpatterns = [
    #Main paths
    path('', views.index, name='index'),

    #Subtabs
    path('fleet', views.fleet, name="fleet"),

    path('weight', views.weight, name='weight'),
    path('remote_hubs_map', views.remote_hubs_map, name='remote_hubs_map'),
    path('get_start_point/<int:company_id>', views.get_start_point, name='get_start_point'),
    path('get_end_point/<int:company_id>', views.get_end_point, name='get_end_point'),
    path('generate_route_google_api_url/<str:waste_type_name>', views.generate_route_google_api_url, name='generate_route_google_api_url'),
    path('show_route_for_waste_type_name/<str:waste_type_name>/', views.show_route_for_waste_type_name, name='show_route_for_waste_type_name'),
    path('show_route', views.show_route, name='show_route')
]