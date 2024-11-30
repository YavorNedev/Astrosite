from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ItemForm
from .models import Item



def shop_view(request):

    categories = Item.CATEGORY_CHOICES


    selected_category = request.GET.get('category')


    if selected_category:
        items = Item.objects.filter(category=selected_category)
    else:
        items = Item.objects.all()

    context = {
        'categories': [category[0] for category in categories],  # Extract category names
        'items': items,
        'selected_category': selected_category,
    }
    return render(request, 'shop/shop_list.html', context)

@login_required
def buy_item(request, pk):

    item = get_object_or_404(Item, pk=pk)
    if item.stock > 0:
        item.stock -= 1
        item.save()
        messages.success(request, f"You have successfully purchased {item.name}!")
    else:
        messages.warning(request, "This item is out of stock.")

    return redirect('shop')


def staff_or_superuser_check(user):
    return user.is_staff or user.is_superuser

@login_required
@user_passes_test(staff_or_superuser_check)
def create_shop_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Shop item created successfully!")
            return redirect('shop')  # Replace 'shop_list' with your shop list view URL name
    else:
        form = ItemForm()

    return render(request, 'shop/create_shop_item.html', {'form': form})



