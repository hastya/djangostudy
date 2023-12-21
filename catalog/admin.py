from django.contrib import admin

from catalog.models import Feedback, Product, Category

# Register your models here.
# admin.site.register(Feedback)
# admin.site.register(Product)
# admin.site.register(Category)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'email')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_price_each', 'product_category', 'is_active')
    list_filter = ('product_category', 'is_active',)
    search_fields = ('product_name', 'product_descr',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('category_name', 'category_descr',)

