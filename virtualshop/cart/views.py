from django.shortcuts import redirect, render, get_object_or_404
from .forms import CartAddProductForm
from .cart import Cart
from django.views.decorators.http import require_POST
from shop.models import Produto

# Create your views here.

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Produto, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            override_quantity=cd['override'],
        )
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Produto, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'override':True}
        )
    return render(request, 'cart/detail.html', {'cart': cart})

def product_detail(request, id, slug):
    product = get_object_or_404(
        Produto, id=id, slug=slug, disponivel=True
    )
    cart_product_form = CartAddProductForm
    return render(
        request, 'shop/produto/detail.html',
        {'produto':product}, {'cart_product_form':cart_product_form}
    )