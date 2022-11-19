from django.http import HttpResponse
from django.conf import settings
import requests

def index(request):
    return HttpResponse("Hello, world. You're at the app index.")

def maps(request):
    with open(settings.GOOGLE_MAPS_API_KEY, 'r') as f:
        google_maps_api_key = f.read()
    response = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=' + google_maps_api_key)
    return HttpResponse(response.content)