from django.core.management import BaseCommand
from main.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        categories = [
            Category(name="Одежда", description="Одежда разных размеров и цветов."),
            Category(name="Электроника", description="Электроника разных брендов и типов."),
        ]
        Category.objects.bulk_create(categories)

        products = [
            Product(name="Футболка", description="Футболка с лого", category=categories[0], price=19.99),
            Product(name="Ноутбук", description="Ноутбук с 8GB RAM и 256GB SSD", category=categories[1],
                    price=599.99),
        ]
        Product.objects.bulk_create(products)
