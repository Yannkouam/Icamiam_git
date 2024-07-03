from django.contrib import admin
from django.urls import path
from icamapps.views import home, event, menu, panier, confirmation, index, add_to_cart, remove_from_cart
from accounts.views import signup, logout_user, login_user
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from icamiam import settings
from django.conf import settings


urlpatterns = [
    path("home/", home, name="home"),
    path('menu/', menu, name='menu'),
    path("event/", event, name="event"),
    path("panier/", panier, name="panier"),
    path('confirmation/<int:product_id>/', confirmation, name='confirmation'),
    path("signup/", signup, name='signup'), 
    path("logout/", logout_user, name='logout'),
    path("login/", login_user, name='login'),
    path('admin/', admin.site.urls), 
    path("", index, name="index"),
    path('panier/add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('panier/remove/<int:order_id>/', remove_from_cart, name='remove_from_cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
