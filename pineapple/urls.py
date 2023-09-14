from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "pineapple"

urlpatterns = [
    path("subscription/create", views.subscription_create_view ,name="subscription-create"),
    path("subscriptions", views.subscription_list_view, name="subscription-list"),

    path('sellers', views.seller_list_view, name='seller-list'),
    path('seller/create', views.seller_create_view, name='seller-create'),
    path('seller/detail/<str:certificate_code>', views.seller_detail_view, name='seller-detail'),
    path('seller/update/<str:certificate_code>', views.seller_update_view, name='seller-update'),

    path('pineapples' ,  views.pineapple_list_view , name = 'pineapple-list'),
    path('pineapple/<int:pk>/detail' ,  views.pineapple_detail_view , name='pineapple-detail'),
    path('pineapple/create' ,  views.pineapple_create_view , name='pineapple-create'),
    path('pineapple/<int:pk>/update' ,  views.pineapple_update_view , name='pineapple-update'),
    path('seller/<int:seller_id>/pineapples' ,  views.seller_pineapple_list_view , name='seller-pineapple-list'),

    path('orders',views.order_list_view,name="order-list"),
    path('order/detail/<int:pk>',views.order_detail_view,name="order-detail"),
    path('order/create',views.order_create_view,name="order-create"),
    path('order/update/<int:pk>',views.order_update_view,name="order-update"),

    path('comment/create', views.comment_create_view,name="comment-create"),
    path('seller/<str:certificate_code>/comments', views.seller_comment_list_view, name="seller-comment-list")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)