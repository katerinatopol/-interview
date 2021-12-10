from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


class ProductsListView(ListView):
    model = Product
    template_name = 'goods_list.html'
    queryset = Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
