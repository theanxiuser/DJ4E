from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# simple response using function
def index(request):
    return HttpResponse("Hello, world. You are in polls index.")
