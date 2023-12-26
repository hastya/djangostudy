from itertools import product

from django.urls import path
from django.contrib import admin

from catalog.apps import CatalogConfig
from catalog.views import homepage, contacts, about, category_idea, ProductListView, CategoryListView, \
    ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, tooggle_activity  # product_detail, CategoryDetailView, index, categories,

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
#    path('<int:pk>/product/', product_detail, name='product_detail'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('activity/<int:pk>/', tooggle_activity, name='tooggle_activity')
]
