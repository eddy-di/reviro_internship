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
