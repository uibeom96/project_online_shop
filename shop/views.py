from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Category, Product

def products_list(request, slug=None):
    current_category = None
    categoris = Category.objects.all()
    products = Product.objects.filter(available_display=True)

    if slug is not None:
        current_category = get_object_or_404(Category, slug=slug)
        products = current_category.products.all()

    return render(request, "shop/products_list.html", 
    {
        "current_category": current_category,
        "categoris": categoris,
        "products": products,
        })


def product_detail(request, pk, slug):
    product = get_object_or_404(Product, id=pk, slug=slug)
    return render(request, "shop/product_detail.html", 
    {
        "product": product
    })

