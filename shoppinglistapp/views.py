from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


# Create your views here.


def get_shopping_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'shoppinglistapp/index.html', context)


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
        # name = request.POST.get('item_name')
        # complete = 'item_complete' in request.POST
        # Item.objects.create(name=name, complete=complete)

        return redirect('get_shopping_list')
    form = ItemForm()
    context = {
        'form': form
    }

    return render(request, 'shoppinglistapp/add_item.html', context)


def edit_item(request, item_id):
    return render(request, 'shoppinglistapp/edit_item.html')

