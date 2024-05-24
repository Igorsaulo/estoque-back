from django.core.management.base import BaseCommand
from faker import Faker, providers
import random
from products.models import Product

class ProductProvider(providers.BaseProvider):
    def product_name(self):
        product_names = [
            'Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Keyboard', 'Mouse',
            'Printer', 'Camera', 'Headphones', 'Speaker', 'Router', 'Smartwatch'
        ]
        return random.choice(product_names) + ' ' + fake.company_suffix()

    def product_description(self):
        descriptions = [
            "High quality product with excellent performance.",
            "Durable and reliable, suitable for all your needs.",
            "State-of-the-art technology for advanced functionality.",
            "Ergonomically designed for comfort and ease of use.",
            "Compact and lightweight, perfect for travel.",
            "Features cutting-edge innovations and sleek design.",
            "Energy-efficient and eco-friendly, saving you money.",
            "Offers seamless connectivity and user-friendly interface.",
            "Built to last with premium materials.",
            "Backed by excellent customer service and support."
        ]
        return random.choice(descriptions)

fake = Faker()
fake.add_provider(ProductProvider)

class Command(BaseCommand):
    help = 'Seed the database with fake data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')
        self.seed_products()
        self.stdout.write('Done.')

    def seed_products(self):
        for _ in range(100):  # Define quantos produtos você quer criar
            Product.objects.create(
                name=fake.product_name(),
                description=fake.product_description(),
                price=round(random.uniform(10.0, 1000.0), 2),
                stock=random.randint(0, 100)
            )
