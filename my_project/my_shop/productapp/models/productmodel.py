from django.db import models
from datetime import date
from .categorymodel import Category
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.db.models import Manager


class Product(models.Model):
    """ Модель продукта """

    name = models.CharField(max_length=255, verbose_name='название')
    received_date = models.DateField(default=date.today, verbose_name='дата поступления')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='цена')
    unit = models.CharField(max_length=10, verbose_name='единица измерения')
    vendor_name = models.CharField(max_length=255, verbose_name='имя поставщика')
    categories = models.ManyToManyField(Category, verbose_name='разделы', related_name='products')
    site = models.ManyToManyField(Site)
    objects = Manager()
    on_site = CurrentSiteManager('site')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']

    def __str__(self):
        return self.name
