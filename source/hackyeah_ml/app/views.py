from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.conf import settings
import requests
from app.logic.remote_hub import RemoteHub as RemoteHubLogic
from app.models import RemoteHub
from app.logic.collector import Collector
import json

def index(request):
    return render(request, "app/index.html")

def fleet(request):

    if request.method == "POST":
        return render(request, "app/fleet.html", {
                "data": "Passwords must match."
            })

    return render(request, "app/fleet.html")

def weight(request):
    return HttpResponse(json.dumps(collector.remote_hubs_data))

def init():
    global collector
    collector = Collector(0)
    print(collector)

init()
