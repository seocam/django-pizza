from django.http import HttpResponse
from django.shortcuts import render

from .models import Pizza


def menu(request):
    pizzas = Pizza.objects.all()
    result = ''
    for pizza in pizzas:
        result += pizza.name
        result += '<br>'
    return HttpResponse(result)
