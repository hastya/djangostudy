from itertools import product

from django.urls import path
from django.contrib import admin

from catalog.apps import CatalogConfig
from catalog.views import homepage, contacts, about, category_idea, ProductListView, CategoryListView, \
    ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, CategoryDetailView, product_detail, tooggle_activity
    # ProductInventView, ProductEditView, index, categories,

app_name = CatalogConfig.name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view(), name='index'),
    path('about/', about, name='about'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
   path('<int:pk>/product/', product_detail, name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('<int:pk>/products/', CategoryDetailView.as_view(), name='category_idea'),
    path('contact/', contacts, name='contacts'),
    path('activity/<int:pk>/', tooggle_activity, name='tooggle_activity')
#    path('<int:pk>/products/', category_idea, name='category_idea'),
#    path('', homepage),
#    path('home/', homepage, name='homepage'),
#    path('', index, name='index'),
#    path('categories/', categories, name='categories')
#    path('invent/', ProductInventView.as_view(), name='invent_product'),
#    path('update/<int:pk>/', ProductEditView.as_view(), name='update_product')
]
