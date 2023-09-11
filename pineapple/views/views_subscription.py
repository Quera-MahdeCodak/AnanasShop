from django.shortcuts import render, redirect

from pineapple.models import Subscription
from pineapple.forms import SubscriptionForm


def subscription_create_view(request):
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pineapple:subscription-list')
    else:
        try:
            form = SubscriptionForm()
        except Exception:
            form = "فرم پیاده سازی نشده است."

    return render(request, 'subscription/subscription_create.html', {'form': form})

def subscription_list_view(request):
    subscriptions = Subscription.objects.all()
    return render(request, 'subscription/subscription_list.html', {'subscriptions': subscriptions})
