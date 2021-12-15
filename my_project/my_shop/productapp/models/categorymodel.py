from django.db import models


class Category(models.Model):
    """
    Модель раздела
    """
    name = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(blank=True, verbose_name='описание')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name
