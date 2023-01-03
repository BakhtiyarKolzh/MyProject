from random import randint
from django.http import HttpRequest, HttpResponse


def show_weather(request: HttpRequest)-> HttpResponse:
    temperature=randint(-40,40)
    feel="OK"
    if temperature>20:
        feel="hot"
    if temperature<0:
        feel="cold"
    if temperature<-10:
        feel="terribly cold"
    return HttpResponse(f"Today {temperature} grad {feel}")
