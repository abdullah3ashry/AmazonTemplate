from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Shop.html', views.shop, name='shop'),
    path('About.html', views.about, name='about'),
    path("product/shop/<int:pk>/", views.product, {"model": "shop"}, name="product_shop"),
    path("product/card/<int:pk>/", views.product, {"model": "card"}, name="product_card"),
    path("product/carousel/<int:pk>/", views.product, {"model": "carousel"}, name="product_carousel"),
    path('Contact.html', views.contact, name='contact')
    ]
