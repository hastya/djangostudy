from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm  # SphereForm,
from catalog.models import Feedback, Product, Category, Version  # Sphere,


# Create your views here.
class ProductListView(ListView):
    model = Product
    # template_name = 'catalog/index.html'
    # template_name = 'catalog/product_list.html'
    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset(*args, **kwargs)
    #     queryset = queryset.filter(is_active=True)
    #     return queryset

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        for product in context['object_list']:
            active_version = product.prod.filter(is_active=True).last()
            if active_version:
                product.active_version_number = active_version.version_number
                product.active_version_name = active_version.name
            else:
                product.active_version_number = None
                product.active_version_name = None
        return context

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
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['object_list'] = Product.objects.filter(pk=self.kwargs['pk'])
    #     return context

# def product_detail(request, pk):
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(id=pk),
#         'title': f'Ideas {product_item.product_name}'
#     }
#     return render(request, 'catalog/product_detail.html', context)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        product = context['object']

        active_version = product.prod.filter(is_active=True).last()
        if active_version:
            product.active_version_number = active_version.version_number
            product.active_version_name = active_version.name
        else:
            product.active_version_number = None
            product.active_version_name = None

        return context

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    # fields = ('product_name', 'product_descr', 'product_img', 'product_category', 'product_price_each')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context_data['formset'] = VersionFormset(self.request.POST)
        else:
            context_data['formset'] = VersionFormset()
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        self.object.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    success_url = reverse_lazy('catalog:index')


class ProductUpdateView(UpdateView):
    model = Product
    # fields = ('product_name', 'product_descr', 'product_img', 'product_category', 'product_price_each')
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()  # для создания обязательно
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    # success_url = reverse_lazy('catalog:product_detail')
    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.object.pk])

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')
    success_message = 'Idea successfully deleted'


def tooggle_activity(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    if product_item.is_active:
        product_item.is_active = False
    else:
        product_item.is_active = True
    product_item.save()
    return redirect(reverse('catalog:index'))


# class ProductInventView(CreateView):
#    model = Product
#    form_class = ProductForm
#    success_url = reverse_lazy('catalog:index')


# class ProductEditView(UpdateView):
#     model = Product
#     form_class = ProductForm
#     success_url = reverse_lazy('catalog:index')
#
#     def get_context_data(self, **kwargs):
#         context_data = super().get_context_data(**kwargs)
#         SphereFormset = inlineformset_factory(Product, Sphere, form=SphereForm, extra=1)
#         if self.request.method == 'POST':
#             context_data['formset'] = SphereFormset(self.request.POST, instance=self.object)
#         else:
#             context_data['formset'] = SphereFormset(instance=self.object)
#         return context_data
#
#
#     def form_valid(self, form):
#         formset = self.get_context_data()['formset']
#         self.object = form.save()
#         if formset.is_valid():
#             formset.instance = self.object
#             formset.save()
#
#         return super().form_valid(form)
