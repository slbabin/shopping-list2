from django.shortcuts import render, HttpResponse
from .models import Item


# Create your views here.


def get_shopping_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'index.html', context)


def add_item(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'add_item.html', context)