from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "pineapple"

urlpatterns = [
    path('subscription-create/' , views.views_subscription.subscription_create_view),
    path('subscription-list/' , views.views_subscription.subscription_list_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)