from django.shortcuts import render, redirect, get_object_or_404


from pineapple.models import Order, Pineapple
from pineapple.forms import OrderForm


def order_list_view(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

def order_detail_view(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'orders/order_detail.html', {'order': order})

def order_create_view(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pineapple:order-list')
    else:
        try:
            form = OrderForm()
        except Exception:
            form = "فرم پیاده سازی نشده است."

    return render(request, 'orders/order_create.html', {'form': form})

def order_update_view(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('pineapple:order-list')
    else:
        try:
            form = OrderForm(instance=order)
        except Exception:
            form = "فرم پیاده سازی نشده است."

    return render(request, 'orders/order_update.html', {'form': form, 'order': order})