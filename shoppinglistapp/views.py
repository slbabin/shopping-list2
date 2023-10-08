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
    if request.method == 'POST':
        name = request.POST.get('item_name')
        complete = 'item_complete' in request.POST
        Item.objects.create(name=name, complete=complete)

        return redirect('get_shopping_list')
    return render(request, 'shoppinglistapp/add_item.html')
