from django.contrib import admin
from django.urls import path
from django.http import HttpRequest, HttpResponse

from views_audi import audi, audi_purchase
from views_name import name
from views_weather import show_weather


def hello_world(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        """
        <h3>Hello, DS!</h3>
        <div style = "font-size: 18px">
            <a href="/weather/">What is the weather today?</a><br>
            <a href="/audi/"> Audi center</a><br>
            <a href="/name"> What is your name?</a>
        </div>
        """)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", hello_world),
    path("weather/", show_weather),
    path("audi/", audi),
    path("buy_car/<int:id_>", audi_purchase),
    path("name/", name),
]
