from django.shortcuts import render, redirect, get_object_or_404

from pineapple.models import Pineapple, Seller
from pineapple.forms import PineappleForm


def pineapple_list_view(request):
    pineapples = Pineapple.objects.all()
    return render(request, 'pineapple/pineapple_list.html', {'pineapples': pineapples})

def seller_pineapple_list_view(request, seller_id):
    seller = Seller.objects.get(pk=seller_id)
    pineapples = Pineapple.objects.filter(seller=seller)
    return render(request, 'pineapple/seller_pineapple_list.html', {'pineapples': pineapples, 'seller': seller})

def pineapple_detail_view(request, pk):
    pineapple = get_object_or_404(Pineapple, pk=pk)
    return render(request, 'pineapple/pineapple_detail.html', {'pineapple': pineapple})

def pineapple_create_view(request):
    if request.method == "POST":
        form = PineappleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pineapple:pineapple-list')
    else:
        try:
            form = PineappleForm()
        except Exception:
            form = "فرم پیاده سازی نشده است."

    return render(request, 'pineapple/pineapple_create.html', {'form': form})

def pineapple_update_view(request, pk):
    pineapple = get_object_or_404(Pineapple, pk=pk)

    if request.method == "POST":
        form = PineappleForm(request.POST, instance=pineapple)
        if form.is_valid():
            form.save()
            return redirect('pineapple:pineapple-list')
    else:
        try:
            form = PineappleForm(instance=pineapple)
        except Exception:
            form = "فرم پیاده سازی نشده است."

    return render(request, 'pineapple/pineapple_update.html', {'form': form, 'pineapple': pineapple})