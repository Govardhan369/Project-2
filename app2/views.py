from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def jampandu(request):
    return HttpResponse('hi how are you')

def jai(request):
    return HttpResponse('I am fine')