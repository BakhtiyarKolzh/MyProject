from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from django.http import HttpRequest, HttpResponse

from views_audi import audi_purchase
from views_name import name
from views_weather import show_weather
from market.views import show_cars


def hello_world(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", hello_world),
    path("weather/", show_weather),
    path("audi/", show_cars),
    path("buy_car/<int:id_>", audi_purchase),
    path("name/", name),
]
