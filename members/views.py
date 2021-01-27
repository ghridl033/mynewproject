from django.shortcuts import render, redirect
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return render(req, 'myproject.html')

