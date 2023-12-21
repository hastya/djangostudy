from django.db import models


NULLABLE = {'blank': True, 'null': True}
# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Сообщение', **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='получено')

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name = 'сообщения'
        ordering = ('name',)


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование')
    product_descr = models.TextField(verbose_name='описание', **NULLABLE)
    product_img = models.ImageField(upload_to='products/', verbose_name='изображение(превью)', **NULLABLE)
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    product_price_each = models.DecimalField(max_digits=3, decimal_places=0, verbose_name='цена за штуку')
    product_date_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    product_date_last = models.DateTimeField(verbose_name='дата последнего изменения', **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='Активно')

    def __str__(self):
        return (f'{self.product_name}')

    class Meta:
        verbose_name = 'продукт'
        verbose_name = 'продукты'
        ordering = ('product_name',)

class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Категория')
    category_descr = models.TextField(verbose_name='Описание', **NULLABLE)
#    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создание')

    is_active = models.BooleanField(default=True, verbose_name='Активно')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name = 'категории'
        ordering = ('category_name',)
