from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("আসসালামু আলাইকুম! এটা আমার প্রথম Django page")