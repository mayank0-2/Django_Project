from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

def home (request) :

    return render (request, 'home_page.html', {})
