from django.core.management import BaseCommand
from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        products_list = [
            {
                "product_name": "Iphone12",
                "product_description": "iphone12",
                "photo": "catalog/Снимок_экрана_от_2023-11-27_19-35-07.png",
                "category_id": 2,
                "price": 80000,
                "creation_date": "2023-11-15",
                "changing_date": "1906-07-20"
            },
            {
                "product_name": "Iphone 13 pro",
                "product_description": "iphone 13 pro",
                "photo": "catalog/Снимок_экрана_от_2023-11-27_19-35-36.png",
                "category_id": 2,
                "price": 110000,
                "creation_date": "2023-11-02",
                "changing_date": "1906-07-12"
            },
            {
                "product_name": "samsung s23 ultra",
                "product_description": "samsung s23 ultra",
                "photo": "",
                "category_id": 2,
                "price": 100000,
                "creation_date": "1906-07-10",
                "changing_date": "1906-07-17"
            },
            {
                "product_name": "Honor Magic 5 Pro",
                "product_description": "Honor Magic 5 Pro",
                "photo": "",
                "category_id": 2,
                "price": 84000,
                "creation_date": "2023-09-13",
                "changing_date": "2023-11-01"
            },
            {
                "product_name": "Google Pixel 7",
                "product_description": "Google Pixel 7",
                "photo": "catalog/Снимок_экрана_от_2023-11-27_19-55-06.png",
                "category_id": 2,
                "price": 46000,
                "creation_date": "2023-10-13",
                "changing_date": "2023-11-13"
            }
        ]

        products_for_create = []
        for product in products_list:
            products_for_create.append(Product.objects.create(**product))

        Product.objects.bulk_create(products_for_create)
