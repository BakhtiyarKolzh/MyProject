from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from market.models import Car


def show_cars(request: HttpRequest) -> HttpResponse:
    context={
        "cars": Car.objects.all()
    }
    return render(request, "cars.html", context)
