from django.db import models

NULLABLE = {'blank': True, 'null': True}

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    text = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='posts/', verbose_name='превью (изображение)', **NULLABLE)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')


    def __str__(self):
        return f'Blog post "{self.title}"\n{self.slug}\n'

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"
        ordering = ('id', 'title')
