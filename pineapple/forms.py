from typing import Any
from django import forms
from .models import *

class SellerForm(forms.Form):
    name = forms.CharField(required=True,label="نام فروشنده",max_length=256)
    address = forms.CharField(required=True,label="آدرس",widget=forms.TextInput)
    certificate_code = forms.CharField(required=True,max_length=10)
    def clean_address(self) -> dict[str, Any]:
        address = self.cleaned_data.get('address')
        if len(address) < 10:
            raise forms.ValidationError("این فیلد باید بیشتر از ۱۰ کاراکتر باشد.")
        return address
    def clean_certificate_code(self) -> dict[str, Any]:
        certificate_code = self.cleaned_data.get('certificate_code')
        if certificate_code != certificate_code.upper():
            raise forms.ValidationError("حروف گواهینامه باید حروف بزرگ باشد.")
        return certificate_code

class PineappleForm(forms.Form):
    price_toman = forms.IntegerField(required=True,label="قیمت هر کیلو آناناس")
    queryset=Seller.objects.all()
    CHOICES = []
    if queryset:
        for obj in queryset:
            choice = (obj.pk,obj.name)
            CHOICES.append(choice)
    seller = forms.ChoiceField(required=True,choices=CHOICES)
    def clean_price_toman(self) -> dict[str, Any]:
        price_toman = self.cleaned_data.get('price_toman')
        if price_toman < 1000:
            raise forms.ValidationError("قیمت نباید کمتر از هزار تومان باشد.")
        if price_toman > 1000000:
            raise forms.ValidationError("قیمت نباید از یک میلیون تومان بیشتر باشد.")
        return price_toman
class OrderForm(forms.Form):
    name = forms.CharField(required=True,label="نام",max_length=50)
    weight_kg = forms.FloatField(label="وزن")
    queryset=Pineapple.objects.all()
    CHOICES = []
    if queryset:
        for obj in queryset:
            choice = (obj.pk,obj.price_toman)
            CHOICES.append(choice)
    pineapple = forms.ChoiceField(required=True,choices=CHOICES)
    def clean_weight_kg(self) -> dict[str, Any]:
        weight_kg = self.cleaned_data.get('weight_kg')
        if weight_kg > 100:
            raise forms.ValidationError("۱۰۰ کیلو آناناس میخوای چیکار؟ مشکل داری؟")
        return weight_kg
class SubscriptionForm(forms.Form):
    name = forms.CharField(required=True,label="نام",max_length=50)
    phone_number = forms.CharField(required=True,label="َشماره تماس",max_length=11)
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if len(phone_number) != 11 or not phone_number.startswith('09'):
            raise forms.ValidationError("شماره تلفن اشتباه است. شماره تلفن باید ۱۱ رقم باشد و با ۰۹ شروع شود.")
        return phone_number

class CommentForm(forms.Form):
    name = forms.CharField(required=True,label="نام",max_length=50)
    text = forms.CharField(required=True,label="متن",widget=forms.Textarea)
    queryset=Seller.objects.all()
    CHOICES = []
    if queryset:
        for obj in queryset:
            choice = (obj.pk,obj.name)
            CHOICES.append(choice)
    seller = forms.ChoiceField(required=True,choices=CHOICES)
    def clean_text(self) -> dict[str, Any]:
        text = self.cleaned_data.get('text')
        if len(text) < 10:
            raise forms.ValidationError("این فیلد باید بیشتر از ۱۰ کاراکتر باشد.")
        return text