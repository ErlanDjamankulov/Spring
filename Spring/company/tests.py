from django.test import TestCase

import pytest
from .models import Company, Product

@pytest.mark.django_db
def test_company_creation():
    company = Company.objects.create(id=1, title="Company 1", description="Description 1", location="Location 1", timetable="Timetable 1")
    assert Company.objects.count() == 1
    assert company.title == "Company 1"

@pytest.mark.django_db
def test_product_creation():
    company = Company.objects.create(id=1, title="Company 1", description="Description 1", location="Location 1", timetable="Timetable 1")
    product = Product.objects.create(title="Product 1", description="Description 1", price=100, stock=10, company=company)
    assert Product.objects.count() == 1
    assert product.title == "Product 1"
