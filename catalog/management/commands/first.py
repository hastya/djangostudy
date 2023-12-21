import json
import os.path

from django.core.management import BaseCommand

from catalog.models import Product, Category
from config.settings import BASE_DIR
from django.shortcuts import get_object_or_404

class Command(BaseCommand):

    def handle(self, *args, **options) -> None:
        Category.objects.all().delete()
        Product.objects.all().delete()

        path_1 = os.path.join(BASE_DIR, 'category_data.json')
        path_2 = os.path.join(BASE_DIR, 'product_data.json')


        with open(path_1) as f:
            file_content = f.read()
            categories_info = json.loads(file_content)
            categories_for_create = []
            for info in categories_info:
                categories_for_create.append(
                    Category(**info["fields"])
                )

            Category.objects.bulk_create(categories_for_create)

        with open(path_2) as f:
            file_content = f.read()
            products_info = json.loads(file_content)
            products_for_create = []
            for info in products_info:
                cat_id = info['fields']['product_category']
                info['fields']['category'] = get_object_or_404(Category, id=cat_id)
                products_for_create.append(
                    Product(**info["fields"])
                )

            Product.objects.bulk_create(products_for_create)
