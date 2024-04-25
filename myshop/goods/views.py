from django.core.paginator import Paginator
from django.shortcuts import render
from goods.models import Categories, Products

def catalog(request, category_id, page=1):

    if category_id == 1:
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category=category_id)

    paginator = Paginator(goods, 6)
    current_page = paginator.page(page)

    context = {
        'title': 'Теремок - Каталог',
        'goods': current_page,
        'category_id': category_id

    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_id):
    product = Products.objects.get(id=product_id)
    context = {
        'product': product,

    }
    return render(request, 'goods/product.html', context)
