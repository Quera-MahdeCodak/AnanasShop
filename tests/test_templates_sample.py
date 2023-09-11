from django.test import TestCase
from django.urls import reverse
from pineapple.models import Subscription, Seller, Pineapple, Order, Comment


class TemplateTestCase(TestCase):
    def setUp(self) -> None:
        # Create test data for the models
        self.seller = Seller.objects.create(
            name="TestSeller",
            address="29334 Hester Ranch Address",
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
    
    # Subscription
    def test_subscription_create(self):
        response = self.client.get(reverse('pineapple:subscription-create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'ثبت نام در خبرنامه')
        self.assertContains(response, 'submit')

    def test_subscription_list(self):
        response = self.client.get(reverse('pineapple:subscription-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'لیست خبرنامه')
        self.assertContains(response, self.subscription.phone_number)
