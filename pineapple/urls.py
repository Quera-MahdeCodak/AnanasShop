from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
app_name = "pineapple"

urlpatterns = [
    path('subscription/create/',subscription_create_view,name="subscription-create"),
    path('subscription/list/',subscription_list_view,name="subscription-list"),
    path('sellers/list/',seller_list_view,name="seller-list"),
    path('sellers/detail/<str:certificate_code>',seller_detail_view,name="seller-detail"),
    path('sellers/create/',subscription_list_view,name="subscription-list"),
    path('sellers/update/<str:certificate_code>',seller_update_view,name="seller-update"),
    path('pineapple/list/',pineapple_list_view,name="pineapple-list"),
    path('pineapple/detail/<int:pk>',pineapple_detail_view,name="pineapple-detail"),
    path('pineapple/create/',pineapple_create_view,name="pineapple-create"),
    path('pineapple/update/<int:pk>',pineapple_update_view,name="pineapple-update"),
    path('seller/<int:pk>/pineapple/list',seller_pineapple_list_view,name="seller-pineapple-list"),
    path('orders/list/',order_list_view,name="order-list"),
    path('orders/detail/<int:pk>',order_detail_view,name="order-detail"),
    path('orders/create/',order_create_view,name="order-create"),
    path('orders/update/<int:pk>',order_update_view,name="order-update"),
    path('comments/create',comment_create_view,name="comment-create"),
    path('seller/<str:certificate_code>/comments/list',seller_comment_list_view,name="seller-comment-list"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)