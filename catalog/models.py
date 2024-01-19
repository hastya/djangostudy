from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

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
        verbose_name_plural = 'сообщения'
        ordering = ('name',)


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование')
    product_descr = models.TextField(verbose_name='описание', **NULLABLE)
    product_img = models.ImageField(upload_to='products/', verbose_name='изображение(превью)', **NULLABLE)
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    product_price_each = models.DecimalField(max_digits=3, decimal_places=0, verbose_name='цена за штуку')
    product_date_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    product_date_last = models.DateTimeField(verbose_name='дата последнего изменения', **NULLABLE)

    # email = models.CharField(max_length=150, verbose_name='email', unique=True, **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    is_active = models.BooleanField(default=True, verbose_name='Активно')

    def __str__(self):
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
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
        verbose_name_plural = 'категории'
        ordering = ('category_name',)


# class Sphere(models.Model):
#     title = models.CharField(max_length=150, verbose_name='Название сферы применения')
#     description = models.TextField(verbose_name='Описание сферы применения')
#
#     product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='продукт')
#     is_active = models.BooleanField(default=True, verbose_name='Активно')
#
#     def __str__(self):
#         return f'{self.title}'
#
#     class Meta:
#         verbose_name = 'сфера'
#         verbose_name_plural = 'сферы'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт', related_name='prod')
    version_number = models.IntegerField(verbose_name="номер версии")
    name = models.CharField(verbose_name="название версии")
    is_active = models.BooleanField(verbose_name="активная версия")

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('product',)
        # constraints = [
        #     models.UniqueConstraint(
        #         fields=['product'],
        #         condition=Q(is_active=True),
        #         name='only_one_active_version_for_product',
        #     ),
        # ]

@receiver(post_save, sender=Version)
def set_current_version(sender, instance, **kwargs):
    if instance.is_active:
        Version.objects.filter(product=instance.product).exclude(pk=instance.pk).update(is_active=False)
