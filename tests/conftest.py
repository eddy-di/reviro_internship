import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from tests.factories import CompanyFactory, ProductFactory

register(CompanyFactory)
register(ProductFactory)


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_num_of_companies_from_factories_without_products(db):

    def make_num_of_companies(num: int = 1) -> list:
        companies = CompanyFactory.create_batch(size=num)
        return companies

    return make_num_of_companies


@pytest.fixture
def company_create_data_dict() -> dict:
    company = {
        'name': 'capito',
        'description': 'coffee house',
        'schedule_start': '08:00:00',
        'schedule_end': '00:00:00',
        'phone_number': '+996558398456',
        'email': 'capito.kg@gmail.com',
        'map_link': 'https://2gis.kg/bishkek/inside/15763234351147898/firm/70000001068507268?m=74.60815%2C42.830919%2F16.57',
        'social_media1': 'https://www.instagram.com/capito.bishkek/',
        'social_media2': 'https://twitter.com/capitobishkek',
        'social_media3': None
    }
    return company


@pytest.fixture
def create_num_of_products_from_factory(db):
    def make_products(num: int) -> list:
        return ProductFactory.create_batch(size=num)
    return make_products


@pytest.fixture
def create_company_from_factory_with_products(db):
    def make_company_with_products(num_products: int = 5):
        company = CompanyFactory.create()
        products = ProductFactory.create_batch(size=num_products, company=company)
        return products
    return make_company_with_products


@pytest.fixture
def product_create_data_dict() -> dict:
    result = {
        'name': 'Random Name',
        'description': 'Random Description',
        'price': '555.55',
        'discount': 0,
        'quantity': 100,
        'company': None,
    }
    return result
