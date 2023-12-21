from itertools import product

from django.urls import path
from django.contrib import admin

from catalog.apps import CatalogConfig
from catalog.views import index, homepage, contacts, about, categories, category_idea, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('admin/', admin.site.urls),
#    path('', homepage),
#    path('home/', homepage, name='homepage'),
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('<int:pk>/products/', category_idea, name='category_idea'),
    path('about/', about, name='about'),
#    path('contact/', contacts, name='contacts'),
    path('<int:pk>/product/', product_detail, name='product_detail')
]
