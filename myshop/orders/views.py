from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render

from carts.models import Cart

from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem


@login_required
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    client = request.user
                    cart_items = Cart.objects.filter(client=client)
                    if cart_items.exists():
                        # Создать заказ
                        order = Order.objects.create(
                            client=client,
                            phone_number=form.cleaned_data['phone_number'],
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )
                        # Создать заказанные товары
                        for cart_item in cart_items:
                            product=cart_item.product
                            price=cart_item.product.price
                            quantity=cart_item.quantity

                            if product.count < quantity:
                                raise ValidationError(f'Недостаточное количество '
                                                      f'товара на складе\
                                                       В наличии - {product.count}')

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                price=price,
                                quantity=quantity,
                            )
                            product.count -= quantity
                            product.save()
                        # Очистить корзину пользователя после создания заказа
                        cart_items.delete()

                        return redirect('client:profile')
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('cart:order')
    else:
        form = CreateOrderForm()
    context = {
        'title': 'Home - Оформление заказа',
        'form': form,
        'orders': True,
    }
    return render(request, 'orders/create_order.html', context=context)
