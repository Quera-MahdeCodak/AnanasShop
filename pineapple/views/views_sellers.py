from django.shortcuts import render, redirect, get_object_or_404

from pineapple.models import Seller
from pineapple.forms import SellerForm


def seller_list_view(request):
    sellers = Seller.objects.all()
    return render(request, 'sellers/seller_list.html', {'sellers': sellers})

def seller_detail_view(request, certificate_code):
    seller = get_object_or_404(Seller, certificate_code=certificate_code)
    return render(request, 'sellers/seller_detail.html', {'seller': seller})

def seller_create_view(request):
    if request.method == "POST":
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pineapple:seller-list') 
    else:
        try:
            form = SellerForm()
        except Exception:
            form = "فرم پیاده سازی نشده است."

    return render(request, 'sellers/seller_create.html', {'form': form})


def seller_update_view(request, certificate_code):
    seller = get_object_or_404(Seller, certificate_code=certificate_code)

    if request.method == "POST":
        form = SellerForm(request.POST, instance=seller)
        if form.is_valid():
            form.save()
            return redirect('pineapple:seller-list')
    else:
        try:
            form = SellerForm(instance=seller)
        except Exception:
            form = "فرم پیاده سازی نشده است."

    return render(request, 'sellers/seller_update.html', {'form': form, 'seller': seller})
