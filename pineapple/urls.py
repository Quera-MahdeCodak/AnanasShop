from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "pineapple"

subscription_patterns = [
    path('subscription/create', views.subscription_create_view, name='subscription-create'),
    path('subscriptions', views.subscription_list_view, name='subscription-list'),
]
seller_patterns = [
    path('sellers', views.seller_list_view,name='seller-list'),
    path('seller/<str:certificateCode>', views.seller_detail_view,name='seller-detail'),
    path('seller/create', views.seller_create_view,name='seller-create'),
    path('seller/update/<str:certificateCode>', views.seller_update_view,name='seller-update'),
]
pineapple_patterns = [
    path('pineapples', views.pineapple_list_view, name='pineapple-list'),
    path('pineapple/<int:pineappleId>', views.pineapple_detail_view, name='pineapple-detail'),
    path('pineapple/create', views.pineapple_create_view, name='pineapple-create'),
    path('pineapple/update/<int:pineappleId>', views.pineapple_update_view, name='pineapple-update'),
    path('seller/<str:certificate_code>/pineapples', views.seller_pineapple_list_view, name='pineapple-update'),
]
order_pattern =[
    path('orders', views.order_list_view,name='order-list'),
    path('order/<int:orderId>', views.order_detail_view,name='order-detail'),
    path('order/create', views.order_create_view,name='order-create'),
    path('order/update/<int:orderId>', views.order_update_view,name='order-update'),
]

urlpatterns = [
    path('', include(subscription_patterns)),
    path('', include(seller_patterns)),
    path('', include(pineapple_patterns)),
    path('', include(order_pattern)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)