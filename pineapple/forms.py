from django import forms
from .models import *

class SellerForm(forms.Form):
    name = forms.CharField(required=True,label="نام فروشنده",max_length=256)
    address = forms.CharField(required=True,label="آدرس",widget=forms.TextInput)
    certificate_code = forms.CharField(required=True,max_length=10)
    def clean_address(self):
        address = self.cleaned_data.get('address')
        if len(address) < 10:
            raise forms.ValidationError("این فیلد باید بیشتر از ۱۰ کاراکتر باشد.")
        return address

class PineappleForm:
    pass

class OrderForm:
    pass

class SubscriptionForm:
    pass

class CommentForm:
    pass