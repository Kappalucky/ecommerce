from apps.store.models import Product
from django.conf import settings

class Cart(object):
    """
    Cart object:
    * init
    * iter
    * len
    * add
    * has_product
    * remove
    * save
    * clear
    * get_total_length
    * get_total_cost
    """
    def __init__(self, request):
        """
        Initialize the cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products from the database.

        """
        print('__iter__')
        product_ids = self.cart.keys()

        product_clean_ids = []

        for p in product_ids:
            product_clean_ids.append(p)

            self.cart[str(p)]['product'] = Product.objects.get(pk=p)

        for item in self.cart.values():
            item['total_price'] = float(item['price']) * int(item['quantity'])

            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity
        """
        product_id = str(product.id)
        price = product.price

        print('Product_id: ', product_id)

        if product_id not in self.cart:
            print('test1')
            self.cart[product_id] = {'quantity': 0,
                                     'price': price, 'id': product_id}

        if update_quantity:
            print('test 2')
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] = self.cart[product_id]['quantity'] + 1

        self.save()

    def has_product(self, product_id):
        if str(product_id) in self.cart:
            return True
        else:
            return False

    def remove(self, product_id):
        """
        Remove a product from the cart.
        """
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        print('save')
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_total_length(self) -> int:
        return sum(int(item['quantity']) for item in self.cart.values())

    def get_total_cost(self):
        return sum(float(item['total_price']) for item in self)