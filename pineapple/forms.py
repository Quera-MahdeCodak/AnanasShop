from django import forms
from .models import *
from django.core.validators import MinLengthValidator,RegexValidator,EmailValidator
from django.core.exceptions import ValidationError


def validate_price_toman(value):
    if value < 1000:
        raise ValidationError('قیمت نباید کمتر از هزار تومان باشد.')
    if value > 1_000_000:
        raise ValidationError('قیمت نباید از یک میلیون تومان بیشتر باشد.')
    return value


def validate_weight_kg(value):
    if value > 100:
        raise ValidationError('۱۰۰ کیلو آناناس میخوای چیکار؟ مشکل داری؟')
    return value


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ["name", "address", "certificate_code"]

    name = forms.CharField(max_length=256)
    address = forms.CharField(
        validators=[
            MinLengthValidator(limit_value=10, message="این فیلد باید بیشتر از ۱۰ کاراکتر باشد.")
        ]
    )
    certificate_code = forms.CharField(
        max_length=10,
        validators=[
            RegexValidator('^[A-Z]+$', message="حروف گواهینامه باید حروف بزرگ باشد.")
        ]
    )


class PineappleForm(forms.ModelForm):
    class Meta:
        model = Pineapple
        fields = ["price_toman", "seller"]

    seller = forms.ModelChoiceField(queryset=Seller.objects.all(),empty_label="فروشنده")
    price_toman = forms.IntegerField(
        label="قیمت",
        validators=[validate_price_toman]
    )


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ["pineapple", "name", "weight_kg"]

    pineapple = forms.ModelChoiceField(queryset=Pineapple.objects.all(),empty_label="آناناس")
    name = forms.CharField()
    weight_kg = forms.FloatField(validators=[validate_weight_kg])


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ["name","phone_number"]

    name = forms.CharField()
    phone_number = forms.CharField(
        validators=[
            RegexValidator('^09[0-9]{9}$',message='شماره تلفن اشتباه است. شماره تلفن باید ۱۱ رقم باشد و با ۰۹ شروع شود.')
        ]
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["seller", "name", "text"]

    seller = forms.ModelChoiceField(queryset=Seller.objects.all(), empty_label="فروشنده")
    name = forms.CharField(max_length=50)
    text = forms.CharField(
        validators=[MinLengthValidator(limit_value=10, message='این فیلد باید بیشتر از ۱۰ کاراکتر باشد.')]
    )
