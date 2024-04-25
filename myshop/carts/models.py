from django.db import models
from clients.models import Client
from goods.models import Products


class CartQueryset(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, blank=True, null=True,
                               verbose_name='Пользователь')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

    objects = CartQueryset().as_manager()

    def products_price(self):
        return round(self.product.price * self.quantity, 2)

    def __str__(self):
        return f'Корзина {self.client.username} | Товар {self.product.name} ' \
               f'| Количество {self.quantity}'

