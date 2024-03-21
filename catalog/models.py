from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Наименование')
    category_description = models.CharField(max_length=100, verbose_name='Описание')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('pk',)


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование')
    product_description = models.CharField(max_length=300, verbose_name='Описание')
    photo = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', **NULLABLE)
    price = models.IntegerField(verbose_name='Цена за штуку')
    creation_date = models.DateField(verbose_name='Дата создания', default='2023-01-01')
    changing_date = models.DateField(verbose_name='Дата последнего изменения', default='2023-01-01')

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Владелец')

    def __str__(self):
        return f'{self.product_name} {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(verbose_name='название версии')
    is_active = models.BooleanField(default=True, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.product} {self.version_name}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
