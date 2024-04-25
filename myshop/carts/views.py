
from carts.models import Cart
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# from carts.utils import get_user_carts
#
#
from goods.models import Products


def cart_add(request, product_id):
    product = Products.objects.get(id=product_id)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(client=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(client=request.user, product=product, quantity=1)

    return HttpResponseRedirect(reverse('mainapp:index'))


def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()

    return HttpResponseRedirect(reverse('mainapp:index'))

