from django.urls import path

from . import views

urlpatterns = [
    #Main paths
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    #Subtabs
    path('fleet', views.fleet, name="fleet")

]