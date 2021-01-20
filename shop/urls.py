from django.urls import path
from shop import views

app_name = "shop"

urlpatterns = [
    path("<str:slug>/", views.products_list, name="in_category_products_list"),
    path("detail/<int:pk>/<str:slug>/", views.product_detail, name="product_detail"),
    path("cart/detail/", views.cart_detail, name="cart_detail"),
    path("cart/add/<int:product_id>/", views.cart_add, name="cart_add"),
    path("cart/remove/<int:product_id>", views.cart_remove, name="cart_remove"),
    path("", views.products_list, name="products_list"),
]