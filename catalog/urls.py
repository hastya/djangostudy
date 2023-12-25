from itertools import product

from django.urls import path
from django.contrib import admin

from catalog.apps import CatalogConfig
from catalog.views import homepage, contacts, about, category_idea, ProductListView, CategoryListView, ProductDetailView # product_detail, CategoryDetailView, index, categories,

app_name = CatalogConfig.name

urlpatterns = [
    path('admin/', admin.site.urls),
#    path('', homepage),
#    path('home/', homepage, name='homepage'),
#    path('', index, name='index'),
    path('', ProductListView.as_view(), name='index'),
#    path('categories/', categories, name='categories'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('<int:pk>/products/', category_idea, name='category_idea'),
#    path('<int:pk>/products/', CategoryDetailView.as_view(), name='category_idea'),
    path('about/', about, name='about'),
#    path('contact/', contacts, name='contacts'),
#    path('<int:pk>/product/', product_detail, name='product_detail')
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product_detail')
]
