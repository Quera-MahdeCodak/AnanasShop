from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "pineapple"

subscription_patterns = [
    path('subscription-create', views.subscription_create_view, name='subscription-create'),
    path('subscription-list', views.subscription_list_view, name='subscription-list'),
]
seller_patterns = [
    path('seller-list', views.seller_list_view,name='seller-list'),
    path('seller-detail/<str:certificateCode>', views.seller_detail_view,name='seller-detail'),
    path('seller-create', views.seller_create_view,name='seller-create'),
    path('seller-update', views.seller_update_view,name='seller-update'),
]
pineapple_patterns = [
    path('pineapple-list', views.pineapple_list_view, name='pineapple-list'),
    path('pineapple-detail/<int:pineappleId>', views.pineapple_detail_view, name='pineapple-detail'),
    path('pineapple-create', views.pineapple_create_view, name='pineapple-create'),
    path('pineapple-update', views.pineapple_update_view, name='pineapple-update'),
    path('seller-pineapple-list/<str:certificate_code>', views.seller_pineapple_list_view, name='pineapple-update'),
]
order_pattern =[
    path('order-list', views.order_list_view,name='order-list'),
    path('order-detail/<int:orderId>', views.order_detail_view,name='order-detail'),
    path('order-create', views.order_create_view,name='order-create'),
    path('order-update', views.order_update_view,name='order-update'),
]

urlpatterns = [
    path('', include(subscription_patterns)),
    path('', include(seller_patterns)),
    path('', include(pineapple_patterns)),
    path('', include(order_pattern)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)