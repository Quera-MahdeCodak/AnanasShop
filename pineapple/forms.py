from django import forms
from .models import *

class SellerForm(forms.Form):
    name = forms.CharField(max_length=256)
    address = forms.TextField()
    certificate_code = forms.CharField(max_length=10)
    
    def clean_certificate_code(self):
        certificate_code = self.cleaned_data['certificate_code']
        if not certificate_code.isupper():
            raise forms.ValidationError('این فیلد باید بیشتر از ۱۰ کاراکتر باشد.')
        return certificate_code
    
    def clean_address(self):
        address = self.cleaned_data['address']
        if len(address) < 10:
            raise forms.ValidationError('حروف گواهینامه باید حروف بزرگ باشد.')
        return address


class PineappleForm(forms.Form):
    price_toman = forms.PositiveIntegerField()
    seller = forms.ForeignKey(Seller, on_delete=models.CASCADE, related_name='pineapple_seler')

    def clean_price_toman(self):
        price = self.cleaned_data['price_toman']
        if price < 1000:
            raise forms.ValidationError('قیمت نباید کمتر از هزار تومان باشد.')
        elif price > 1000000:
            raise forms.ValidationError('قیمت نباید از یک میلیون تومان بیشتر باشد.')
        return price

class OrderForm(forms.Form):
    pineapple = forms.ModelChoiceField(Pineapple, on_delete=models.CASCADE, related_name='pineapple_seler')
    name = models.CharField(max_length=50)
    weight_kg = models.FloatField()

    def clean_weight_kg(self):
        weight_kg = self.cleaned_data['weight_kg']
        if weight_kg > 100:
            raise forms.ValidationError('۱۰۰ کیلو آناناس میخوای چیکار؟ مشکل داری؟')
        return weight_kg   



class SubscriptionForm(forms.Form):
    name = forms.CharField(max_length=50)
    phone_number = forms.CharField()
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if len(phone_number) != 11 or phone_number[0:3] != '09':
            raise forms.ValidationError('شماره تلفن اشتباه است. شماره تلفن باید ۱۱ رقم باشد و با ۰۹ شروع شود.')
        return phone_number   

class CommentForm(forms.Form):
    seller = forms.ModelChoiceField(Seller, on_delete=models.CASCADE)
    name = forms.CharField(max_length=50)
    text = forms.TextField()
    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) < 10:
            raise forms.ValidationError('این فیلد باید بیشتر از ۱۰ کاراکتر باشد.')
        return text
