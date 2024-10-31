from decimal import Decimal
from django.conf import settings
from shop.models import Produto

class Cart:
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            #Salva um carrinho vazio na sessão do browser
            cart = self.session[settings.CART_SSESIONS_ID] = {}
        self.cart = cart
    
    def add(self, product, quantity=1, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price),
            }
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        
        self.save()
    
    def save(self):
        #Marca a sessão como modificada
        #para ter certerza que será salva
        self.session.modified = True
    
    def __iter__(self):
        """
        Interage sobre os itens do carrinho e obtem os produtos da base de dados.
        """
        products_ids = self.cart.keys()
        #get the product objects and add to the cart
        products = Produto.objects.filter(id__in=products_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item #return a list of values from this function
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        #remove o carrinho da sessão
        del self.session[settings.CART_SESSION_ID]
        self.save()
    
    def get_total_price(self):
        return sum(
            Decimal (item['price']) * item['quantity']
            for item in self.cart.values()
        )