from django.test import TestCase
from pineapple.forms import *
from pineapple.models import Seller, Pineapple


class FormValidationTest(TestCase):
    def setUp(self) -> None:
        # Create test data for the models
        self.seller = Seller.objects.create(
            name="TestSeller",
            address="Test Address",
            certificate_code="123456"
        )
        
        self.pineapple = Pineapple.objects.create(
            price_toman=100,
            seller=self.seller
        )
        
        self.seller1 = {
            'name': "TestSeller",
            'address': "Test",
            'certificate_code': "CSWECX"
        }

        self.seller2 = {
            'name': "TestSeller",
            'address': "Quera QueraNejad Road",
            'certificate_code': "CSWECX"
        }

        self.seller3 = {
            'name': "TestSeller",
            'address': "Quera QueraNejad Road",
            'certificate_code': "CSWECx"
        }
        
        self.pineapple1 = {
            'price_toman': 100,
            'seller': self.seller
        }
        self.pineapple2 = {
            'price_toman': 10000050,
            'seller': self.seller
        }
        self.pineapple3 = {
            'price_toman': 5000,
            'seller': self.seller
        }
        
        self.order1 = {
            'pineapple': self.pineapple,
            'name': "Test Order",
            'weight_kg': 50
        }
        self.order2 = {
            'pineapple': self.pineapple,
            'name': "Test Order",
            'weight_kg': 150
        }

        self.comment = {
            'seller': self.seller,
            'name': "Test Comment",
            'text': "This"
        }
        
        self.subscription1 = {
            'name': "Test Subscriber",
            'phone_number': "12345678901"
        }

        self.subscription2 = {
            'name': "Test Subscriber",
            'phone_number': "09114412191"
        }

    def test_comment_form(self):
        form = CommentForm(data=self.comment)
        self.assertFalse(form.is_valid())

    def test_seller_form(self):
        form1 = SellerForm(data=self.seller1)
        self.assertFalse(form1.is_valid())

        form3 = SellerForm(data=self.seller3)
        self.assertFalse(form3.is_valid())

        form2 = SellerForm(data=self.seller2)
        self.assertTrue(form2.is_valid())

    def test_pineapple_form(self):
        form1 = PineappleForm(data=self.pineapple1)
        self.assertFalse(form1.is_valid())

        form2 = PineappleForm(data=self.pineapple2)
        self.assertFalse(form2.is_valid())

        form3 = PineappleForm(data=self.pineapple3)
        self.assertTrue(form3.is_valid())

    def test_order_form(self):
        form1 = OrderForm(data=self.order1)
        self.assertTrue(form1.is_valid())
        form2 = OrderForm(data=self.order2)
        self.assertFalse(form2.is_valid())

    def test_subscription_form(self):
        form1 = SubscriptionForm(data=self.subscription1)
        self.assertFalse(form1.is_valid())
        form2 = SubscriptionForm(data=self.subscription2)
        self.assertTrue(form2.is_valid())

