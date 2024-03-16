import pytest
from rest_framework.reverse import reverse


@pytest.mark.django_db
def test_company_list_api(
    api_client
):
    # given unauthorized client and empty db
    client = api_client
    # when client accessing the companies list endpoint
    url = reverse('companies')
    response = client.get(url)
    # then expecting empty list in results and status 200
    print(response.content.decode('utf-8'))
    assert response.status_code == 200
    assert response.data['results'] == []


@pytest.mark.django_db
def test_company_list_api_with_companies(
    api_client,
    create_num_of_companies_from_factories_without_products
):
    # given unauthorized client and not empty db
    client = api_client
    create_num_of_companies_from_factories_without_products(20)
    # when client accessing the companies list endpoint
    url = reverse('companies')
    response = client.get(url)
    # then expecting not empty list in results and status 200
    print(response.content.decode('utf-8'))
    assert response.status_code == 200
    assert len(response.data['results']) == 10
