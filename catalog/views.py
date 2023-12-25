from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Feedback, Product, Category


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_active=True)
        return queryset


# def index(request):
# #    products_info = Product.objects.all()
# #    feedback_list = Feedback.objects.filter(is_active=True)
#     context = {
# #        'object_list': Category.objects.filter(is_active=True)[:3],
#         'object_list': Product.objects.filter(is_active=True),
#         'title': 'Ideas Store'
#     }
#     return render(request, 'catalog/index.html', context)

def about(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'catalog/about.html')

def homepage(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'catalog/contacts.html')


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/categories.html'

# def categories(request):
#     context = {
#         'object_list': Category.objects.filter(is_active=True),
#         'title': 'Ideas Categories'
#     }
#     return render(request, 'catalog/categories.html', context)

# class CategoryDetailView(DetailView):
#     model = Product
#     template_name = 'catalog/products.html'
#     def get_queryset(self, *args, **kwargs):
#         queryset = super().get_queryset(*args, **kwargs)
#         queryset = queryset.filter(is_active=True)
#         return queryset

def category_idea(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(product_category_id=pk),
        'title': f'Ideas {category_item.category_name}'
    }
    return render(request, 'catalog/products.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Product.objects.filter(pk=self.kwargs['pk'])
        return context

# def product_detail(request, pk):
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(id=pk),
#         'title': f'Ideas {product_item.product_name}'
#     }
#     return render(request, 'catalog/product_detail.html', context)
