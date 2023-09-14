from django.shortcuts import render, redirect, get_object_or_404

from pineapple.models import Seller
from pineapple.forms import SellerForm


def seller_list_view(request):
    sellers = Seller.objects.all()
    context = {'sellers': sellers}
    return render(request, 'sellers/seller_list.html', context)

def seller_detail_view(request, certificate_code):
    seller = get_object_or_404(Seller, certificate_code=certificate_code)
    return render(request, 'sellers/seller_detail.html', {'seller': seller})

def seller_create_view(request):
    form = SellerForm()
    if request.method == "POST":
        form = SellerForm(request.POST)
        if form.is_valid():
            obj = Seller.objects.create(name=form.cleaned_data['name'],address=form.cleaned_data['address'],certificate_code=form.cleaned_data['certificate_code'])
            obj.save()
            return redirect('pineapple:seller-list') 
    else:
        try:
            form = SellerForm()
        except Exception:
            form = "فرم پیاده سازی نشده است."
    context = {'form': form}
    return render(request, 'sellers/seller_create.html', context)


def seller_update_view(request, certificate_code):
    seller = get_object_or_404(Seller, certificate_code=certificate_code)
    obj = Seller.objects.filter(certificate_code=certificate_code)
    if request.method == "POST":
        form = SellerForm(request.POST, instance=seller)
        if form.is_valid():
            data = form.cleaned_data
            obj.update(**data)
            return redirect('pineapple:seller-list')
    else:
        try:
            form = SellerForm(instance=seller)
        except Exception:
            form = "فرم پیاده سازی نشده است."

    return render(request, 'sellers/seller_update.html', {'form': form, 'seller': seller})
