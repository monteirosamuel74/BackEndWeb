from django.shortcuts import get_object_or_404, render

from cart.forms import CartAddProductForm
from .models import Categoria, Produto

# Create your views here.
def produto_list(request, categoria_slug=None):
    categoria = None
    categorias = Categoria.objects.all()
    produtos = Produto.objects.filter(disponivel=True)
    if categoria_slug:
        categoria = get_object_or_404(Categoria, slug = categoria_slug)
        produtos = produtos.filter(categoria = categoria)
    return render(
        request,
        'shop/produto/list.html',
        {
            'categoria': categoria,
            'categorias': categorias,
            'produtos': produtos
        }
    )

def produto_detalhe(request, id, slug):
    produto = get_object_or_404(
        Produto, id = id, slug = slug, disponivel = True
    )
    cart_product_form = CartAddProductForm
    return render(
        request,
        'shop/produto/detail.html',
        {'produto': produto},
        {'cart_product_form':cart_product_form}
    )
