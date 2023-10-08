from django.shortcuts import render, redirect
from .models import Item


# Create your views here.


def get_shopping_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'shoppinglistapp/index.html', context)


def add_item(request):

    return render(request, 'shoppinglistapp/add_item.html')
