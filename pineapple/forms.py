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


class PineappleForm(forms.ModelForm):
    class Meta:
        model = Pineapple
        fields = '__all__'


    def clean_price_toman(self):
        price_toman = self.cleaned_data.get('price_toman')
        if price_toman < 1000:
            raise forms.ValidationError("قیمت نباید کمتر از هزار تومان باشد.")
        if price_toman > 1000000:
            raise forms.ValidationError("قیمت نباید از یک میلیون تومان بیشتر باشد.")
        return price_toman

class OrderForm:
    class Meta:
        model = Order
        fields = '__all__'
    
    def clean_weight_kg(self):
        weight_kg = self.cleaned_data.get('weight_kg')
        if weight_kg > 100:
            raise forms.ValidationError("۱۰۰ کیلو آناناس میخوای چیکار؟ مشکل داری؟")
        return weight_kg


class SubscriptionForm:
    pass

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) < 10:
            raise forms.ValidationError('این فیلد باید بیشتر از ۱۰ کاراکتر باشد.')
        return text

