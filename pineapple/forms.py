from django import forms
from .models import *
import re

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = "__all__"
    
    def clean_certificate_code(self):
        certificate_code = self.cleaned_data['certificate_code']
        if not certificate_code.isupper():
            raise forms.ValidationError('حروف گواهینامه باید حروف بزرگ باشد.')
        return certificate_code
    
    def clean_address(self):
        address = self.cleaned_data['address']
        if len(address) < 10:
            raise forms.ValidationError('این فیلد باید بیشتر از ۱۰ کاراکتر باشد.')
        return address

class PineappleForm:
    pass

class OrderForm:
    pass

class SubscriptionForm:
    pass

class CommentForm:
    pass