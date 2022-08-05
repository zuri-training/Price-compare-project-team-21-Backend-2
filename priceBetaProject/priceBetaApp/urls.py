from django.urls import path
from . import views
from .views import Product, Category, Wishlist, Store


urlpatterns = [
	path('index', views.index, name = "index"),
	path('', Product),
    path('', Category),
    path('', Store),
    path('', Wishlist)
]
