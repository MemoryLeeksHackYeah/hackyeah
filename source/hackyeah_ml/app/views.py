from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.conf import settings
import requests
from .models import RemoteHub as RealRemoteHub
from app.models import RemoteHub
from app.logic.collector import Collector
import json

def index(request):
    return render(request, "app/index.html")

def fleet(request):
    return render(request, "app/fleet.html")

def weight(request):
    collector.update_remote_hubs_data()
    return HttpResponse(json.dumps(collector.remote_hubs_data))

def init():
    global collector
    collector = Collector(0)
    print(collector)

init()

def remote_hubs_map(request):
    collector.update_remote_hubs_data()
    data = collector.remote_hubs_data
    points_on_map = []
    if request.method == 'GET':
        for remote_hub_details in data.values():
            hub_id = remote_hub_details['id']
            weights_type_ready_to_empty = {}
            if hub_id == 0:
                real_remote_hub = RealRemoteHub.objects.get(id=0)
                lat = real_remote_hub.location_latitude
                long = real_remote_hub.location_longitude
                for weight_details in remote_hub_details['weights']:
                    if weight_details['type'] == 'mixed':
                        weights_type_ready_to_empty[weight_details['type']] = weight_details['weight'] / (5.0 * 0.667)
                    elif weight_details['type'] == 'plastic':
                        weights_type_ready_to_empty[weight_details['type']] = weight_details['weight'] / (5.0 * (1.0 - 0.667))
                    else:
                        raise TypeError("Not valid trash type!")
                points_on_map.append((long, lat, weights_type_ready_to_empty))
            else:
                lat = remote_hub_details['lat']
                long = remote_hub_details['long']
                for weight_details in remote_hub_details['weights']:
                    weights_type_ready_to_empty[weight_details['type']] = weight_details['weight'] / 1500.0
                points_on_map.append((long, lat, weights_type_ready_to_empty))
        return HttpResponse(points_on_map)

def show_route_for_waste_type_name(request, waste_type_name):
    collector.update_remote_hubs_data()
    data = collector.remote_hubs_data
    points_on_map = []
    if request.method == 'GET':
        for remote_hub_details in data.values():
            hub_id = remote_hub_details['id']
            weights_type_ready_to_empty = {}
            if hub_id == 0:
                real_remote_hub = RealRemoteHub.objects.get(id=0)
                lat = real_remote_hub.location_latitude
                long = real_remote_hub.location_longitude
                for weight_details in remote_hub_details['weights']:
                    if weight_details['type'] == 'mixed':
                        weights_type_ready_to_empty['mixed'] = weight_details['weight'] / (5.0 * 0.667)
                    elif weight_details['type'] == 'plastic':
                        weights_type_ready_to_empty['plastic'] = weight_details['weight'] / (5.0 * (1.0 - 0.667))
                    else:
                        raise TypeError("Not valid trash type!")
                points_on_map.append((long, lat, weights_type_ready_to_empty))
            else:
                lat = remote_hub_details['lat']
                long = remote_hub_details['long']
                for weight_details in remote_hub_details['weights']:
                    weights_type_ready_to_empty[weight_details['type']] = weight_details['weight'] / 1500.0
                points_on_map.append((long, lat, weights_type_ready_to_empty))
        points_to_make_a_route=[]
        for point in points_on_map:
            if waste_type_name in point[2] and point[2][waste_type_name] > 0.65:
                points_to_make_a_route.append(point)
        return HttpResponse(points_to_make_a_route)

# def generate_

def show_route(request):
    return render(request, "app/show_route.html")

