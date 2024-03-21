import json

import pytest
from rest_framework.reverse import reverse


@pytest.mark.django_db
def test_get_product_list_with_empty_products(
    api_client,
    create_num_of_companies_from_factories_without_products
):
    # given unauthed client and a company without products
    client = api_client
    company = create_num_of_companies_from_factories_without_products(1)[0]
    # when accessing products api
    url = reverse(
        'products',
        kwargs={
            'company_id': company.id
        }
    )
    response = client.get(url)
    print(response.content.decode('utf-8'))
    # then expecting status code 200 and empty results
    assert response.status_code == 200
    assert response.data['results'] == []


@pytest.mark.django_db
def test_get_product_list_with_one_product(
    api_client,
    create_num_of_products_from_factory
):
    # given unauthed client and a product with company
    client = api_client
    product = create_num_of_products_from_factory(1)[0]
    # when accessing the api
    url = reverse('products', kwargs={'company_id': product.company.id})
    response = client.get(url)
    # then expecting status code 200 and product info
    assert response.status_code == 200
    assert response.data['results'][0]['name'] == product.name
    assert response.data['results'][0]['description'] == product.description
    assert response.data['results'][0]['price'] == str(product.price)
    assert response.data['results'][0]['discount'] == product.discount
    assert response.data['results'][0]['quantity'] == product.quantity
    assert response.data['results'][0]['company'] == product.company.id


@pytest.mark.django_db
def test_get_products_list_with_one_company_and_many_products(
    api_client,
    create_company_from_factory_with_products
):
    # given unauthed client and
    client = api_client
    products = create_company_from_factory_with_products(15)
    first_product = products[0]
    # when accessing api
    url = reverse('products', kwargs={'company_id': products[0].company.id})
    response = client.get(url)
    # then expecting status code 200 and 10 products per one page for a single company
    assert response.status_code == 200
    assert len(response.data['results']) == 10
    assert response.data['results'][0]['name'] == first_product.name
    assert response.data['results'][0]['description'] == first_product.description
    assert response.data['results'][0]['price'] == str(first_product.price)
    assert response.data['results'][0]['discount'] == first_product.discount
    assert response.data['results'][0]['quantity'] == first_product.quantity


@pytest.mark.django_db
def test_post_product_list_api(
    api_client,
    create_num_of_companies_from_factories_without_products,
    product_create_data_dict
):
    # given unauthed client and
    client = api_client
    company = create_num_of_companies_from_factories_without_products(1)[0]
    product_post_data = product_create_data_dict
    product_post_data['company'] = company.id
    # when accessing api to create product
    url = reverse('products', kwargs={'company_id': company.id})
    response = client.post(
        url,
        data=json.dumps(product_post_data),
        content_type='application/json'
    )
    # then expecting status code 201 and given product_post_data
    assert response.status_code == 201
    assert response.data['name'] == product_post_data['name']
    assert response.data['description'] == product_post_data['description']
    assert response.data['price'] == product_post_data['price']
    assert response.data['discount'] == product_post_data['discount']
    assert response.data['quantity'] == product_post_data['quantity']
    assert response.data['company'] == product_post_data['company']


@pytest.mark.django_db
def test_get_specific_product(
    api_client,
    create_company_from_factory_with_products
):
    # given unauthed client and
    client = api_client
    products = create_company_from_factory_with_products(20)
    product1 = products[0]
    # when accessing api
    url = reverse(
        'product_details',
        kwargs={
            'company_id': product1.company.id,
            'product_id': product1.id
        }
    )
    response = client.get(url)
    # then expecting status code 200 and specific products data
    assert response.status_code == 200
    assert response.data['name'] == product1.name
    assert response.data['description'] == product1.description
    assert response.data['price'] == str(product1.price)
    assert response.data['discount'] == product1.discount
    assert response.data['quantity'] == product1.quantity
    assert response.data['company'] == product1.company.id


@pytest.mark.django_db
def test_patch_specific_product(
    api_client,
    create_company_from_factory_with_products
):
    # given unauthed client and
    client = api_client
    product = create_company_from_factory_with_products(1)[0]
    patch_data = {
        'name': 'Patched name',
        'description': 'Patched description'
    }
    # when accessing api
    url = reverse(
        'product_details',
        kwargs={
            'company_id': product.company.id,
            'product_id': product.id
        }
    )
    response = client.patch(
        url,
        data=json.dumps(patch_data),
        content_type='application/json'
    )
    # then expecting status code 200 and pathed products data
    assert response.status_code == 200
    assert response.data['name'] == patch_data['name']
    assert response.data['description'] == patch_data['description']
    assert response.data['price'] == str(product.price)
    assert response.data['discount'] == product.discount
    assert response.data['quantity'] == product.quantity
    assert response.data['company'] == product.company.id


@pytest.mark.django_db
def test_put_specific_product(
    api_client,
    create_company_from_factory_with_products
):
    # given unauthed client and
    client = api_client
    product = create_company_from_factory_with_products(1)[0]
    put_data = {
        'name': 'Update PUT name',
        'description': 'Update PUT description',
        'price': '333.33',
        'discount': 0,
        'quantity': 10
    }
    # when accessing api
    url = reverse(
        'product_details',
        kwargs={
            'company_id': product.company.id,
            'product_id': product.id
        }
    )
    response = client.patch(
        url,
        data=json.dumps(put_data),
        content_type='application/json'
    )
    # then expecting status code 200 and product afte put_data
    assert response.status_code == 200
    assert response.data['name'] == put_data['name']
    assert response.data['description'] == put_data['description']
    assert response.data['price'] == put_data['price']
    assert response.data['discount'] == put_data['discount']
    assert response.data['quantity'] == put_data['quantity']


@pytest.mark.django_db
def test_delete_specific_product(
    api_client,
    create_company_from_factory_with_products
):
    # given unauthed client and
    client = api_client
    product = create_company_from_factory_with_products(1)[0]
    # when accessing api
    url = reverse(
        'product_details',
        kwargs={
            'company_id': product.company.id,
            'product_id': product.id
        }
    )
    response = client.delete(url)
    # then expecting status code 200 and None/null as a result
    assert response.status_code == 204
    assert response.data == None
