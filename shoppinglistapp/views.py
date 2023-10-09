from django.shortcuts import render, redirect, get_object_or_404
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
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()

        return redirect('get_shopping_list')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'shoppinglistapp/edit_item.html', context)


def item_status(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.complete = not item.complete
    item.save()
    return redirect('get_shopping_list')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_shopping_list')
