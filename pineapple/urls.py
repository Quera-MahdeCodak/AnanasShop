from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "pineapple"

urlpatterns = [
    path("subscription/create", views.subscription_create_view ,name="subscription-create"),
    path("subscriptions", views.subscription_list_view, name="subscription-list"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)