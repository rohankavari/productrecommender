import os
import django
from django.conf import settings

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom_recommendation.settings')
django.setup()

# Your script code here
from ecom_recommendation.ecom.models import Product
import random

def clear_products():
    # Clear all existing products
    Product.objects.all().delete()

def generate_products():
    products = [
        {"name": "toothpaste", "sizes": ["100g", "250g", "500g"]},
        {"name": "toothbrush", "sizes": ["100g", "250g", "500g"]},
        {"name": "washing powder", "sizes": ["100g", "250g", "500g"]},
        {"name": "soap", "sizes": ["100g", "250g", "500g"]},
        {"name": "handwash", "sizes": ["100g", "250g", "500g"]}
    ]
    locations = ["Pune", "Mumbai"]

    total_products = 1000000
    batch_size = 1000  # Adjust batch size based on your system resources

    batches = total_products // batch_size

    for _ in range(batches):
        batch_products = []
        for _ in range(batch_size):
            product_info = random.choice(products)
            size = random.choice(product_info["sizes"])
            location = random.choice(locations)
            price = random.randint(100, 500)
            product = Product(name=product_info["name"], size=size, location=location, price=price)
            batch_products.append(product)

        Product.objects.bulk_create(batch_products)

    # Create remaining products for the last batch
    remaining_products = total_products % batch_size
    if remaining_products:
        batch_products = []
        for _ in range(remaining_products):
            product_info = random.choice(products)
            size = random.choice(product_info["sizes"])
            location = random.choice(locations)
            price = random.randint(100, 500)
            product = Product(name=product_info["name"], size=size, location=location, price=price)
            batch_products.append(product)

        Product.objects.bulk_create(batch_products)

if __name__ == "__main__":
    clear_products()  # Clear existing products before generating new ones
    generate_products()
