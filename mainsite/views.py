from django.shortcuts import render
from .models import *

def index(request):
    tables = TableFurniture.objects.all()
    return render(request, 'index.html', {"items": range(7)})