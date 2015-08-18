from django.http import HttpResponse
from django.shortcuts import render


def menu(request):
    return HttpResponse('Hello World')
