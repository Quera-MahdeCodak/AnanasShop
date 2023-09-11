from django.test import TestCase
from pineapple.forms import CommentForm
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
            'certificate_code': "CSWECx"
        }

        self.seller2 = {
            'name': "TestSeller",
            'address': "Quera QueraNejad Road",
            'certificate_code': "CSWECX"
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
        
        self.order = {
            'pineapple': self.pineapple,
            'name': "Test Order",
            'weight_kg': 150
        }
        
        
        self.comment = {
            'seller': self.seller,
            'name': "Test Comment",
            'text': "This"
        }
        
        self.subscription = {
            'name': "Test Subscriber",
            'phone_number': "12345678901"
        }

    def test_comment_form(self):
        form = CommentForm(data=self.comment)
        self.assertFalse(form.is_valid())
