from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "pineapple"

urlpatterns = [
    path('subscription-create/' , views.views_subscription.subscription_create_view , name ='subscription-create'),
    path('subscription-list/' , views.views_subscription.subscription_list_view , name = 'subscription-list'),
    path('seller-list/' , views.views_sellers.seller_list_view , name='seller-list'),
    path('seller-create' , views.views_sellers.seller_create_view , name='seller-create'),
    path('seller-detail/<int:certificate_code>' , views.views_sellers.seller_detail_view , name='seller-detail'),
    path('seller-update/<int:certificate_code>' , views.views_sellers.seller_update_view , name='seller-update'),

    path('pineapple-list/' , views.views_pineapple.pineapple_list_view , name = 'pineapple-list'),
    path('pineapple-detail/<int:pk>/' , views.views_pineapple.pineapple_detail_view , name='pineapple-detail'),
    path('pineapple-create/' , views.views_pineapple.pineapple_create_view , name='pineapple-create'),
    path('pineapple-update/<int:pk>' , views.views_pineapple.pineapple_update_view , name='pineapple-update'),
    path('seller-pineapple-list/<int:seller_id>' , views.views_pineapple.seller_pineapple_list_view , name='seller-pineapple-list'),
    
    path('order-list/' , views.views_sellers.seller_list_view , name='order-list'),
    path('order-create' , views.views_sellers.seller_create_view , name='order-create'),
    path('order-detail/<int:pk>' , views.views_sellers.seller_detail_view , name='order-detail'),
    path('order-update/<int:pk>' , views.views_sellers.seller_update_view , name='order-update'),

    path('comment-create/' , views.views_comments.comment_create_view , name = 'comment-create'),
    path('seller-comment-list' , views.views_comments.seller_comment_list_view , name='seller-comment-list')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)