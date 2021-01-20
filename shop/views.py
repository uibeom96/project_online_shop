from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Category, Product
from django.views.decorators.http import require_POST
from shop.cart import Cart
from shop.forms import AddProductForm


def products_list(request, slug=None):
    current_category = None
    categoris = Category.objects.all()
    products = Product.objects.filter(available_display=True)


    if slug is not None:
        current_category = get_object_or_404(Category, slug=slug)
        products = current_category.products.all()

    if request.GET.get("search_input"):
        if current_category :
            products = current_category.products.filter(title__contains=request.GET.get("search_input"))
        else:
            products = Product.objects.filter(title__contains=request.GET.get("search_input"))
        return render(request, "shop/products_search_list.html", 
        {
            "current_category": current_category,
            "categoris": categoris,
            "products": products
        })

    return render(request, "shop/products_list.html", 
    {
        "current_category": current_category,
        "categoris": categoris,
        "products": products,
        })


def product_detail(request, pk, slug):
    product = get_object_or_404(Product, id=pk, slug=slug)
    add_to_cart = AddProductForm(initial={"quantity": 1})
    return render(request, "shop/product_detail.html", 
    {
        "product": product,
        "add_to_cart": add_to_cart,
    })


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    form = AddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], is_update=cd['is_update'])

    return redirect('shop:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('shop:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for product in cart:
        product['quantity_form'] = AddProductForm(initial={'quantity':product['quantity'], 'is_update':True})
    return render(request, 'shop/cart_detail.html', {'cart':cart})

            