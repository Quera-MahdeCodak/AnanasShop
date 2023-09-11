from django.test import TestCase
from django.urls import reverse
from pineapple.models import Subscription, Seller, Pineapple, Order, Comment


class UrlTestCase(TestCase):
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
        
        self.order = Order.objects.create(
            pineapple=self.pineapple,
            name="Test Order",
            weight_kg=1.5
        )
        
        self.comment = Comment.objects.create(
            seller=self.seller,
            name="Test Comment",
            text="This is a test comment."
        )
        
        self.subscription = Subscription.objects.create(
            name="Test Subscriber",
            phone_number="12345678901"
        )

    # Pineapple
    def test_pineapple_list(self):
        response = self.client.get(reverse('pineapple:pineapple-list'))
        self.assertEqual(response.status_code, 200)
