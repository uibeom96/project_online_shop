from django.urls import path
from shop import views

app_name = "shop"

urlpatterns = [
    path("<str:slug>/", views.products_list, name="in_category_products_list"),
    path("detail/<int:pk>/<str:slug>/", views.product_detail, name="product_detail"),
    path("", views.products_list, name="products_list"),
]