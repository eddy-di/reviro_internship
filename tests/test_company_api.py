import json

import pytest
from rest_framework.reverse import reverse


@pytest.mark.django_db
def test_get_company_list_api_with_empty_companies(
    api_client
):
    # given unauthorized client and empty db
    client = api_client
    # when client accessing the companies list endpoint
    url = reverse('companies')
    response = client.get(url)
    # then expecting empty list in results and status 200
    assert response.status_code == 200
    assert response.data['results'] == []


@pytest.mark.django_db
def test_get_company_list_api_with_companies(
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
    assert response.status_code == 200
    assert len(response.data['results']) == 10


@pytest.mark.django_db
def test_post_company_create_api(
    api_client,
    company_create_data_dict
):
    # given unauthorized client and dict data for example company
    client = api_client
    company_post_data = company_create_data_dict
    # when creating company
    url = reverse('companies')
    response = client.post(
        url,
        data=json.dumps(company_post_data),
        content_type='application/json'
    )
    # then expecting to get code 201 and created comapny data in results
    assert response.status_code == 201
    assert response.data['name'] == company_post_data['name']
    assert response.data['description'] == company_post_data['description']
    assert response.data['schedule_start'] == company_post_data['schedule_start']
    assert response.data['schedule_end'] == company_post_data['schedule_end']
    assert response.data['phone_number'] == company_post_data['phone_number']
    assert response.data['email'] == company_post_data['email']
    assert response.data['map_link'] == company_post_data['map_link']
    assert response.data['social_media1'] == company_post_data['social_media1']
    assert response.data['social_media2'] == company_post_data['social_media2']


@pytest.mark.django_db
def test_get_company_specific_api_for_non_existent_company(
    api_client
):
    # given an unauthed client
    client = api_client
    # when client is trying to access empty db
    url = reverse(
        'company_details',
        kwargs={
            'company_id': 1
        }
    )
    response = client.get(url)
    # then expecting to get 404 and not fund message
    assert response.status_code == 404
    assert response.data['detail'] == 'Not found.'


@pytest.mark.django_db
def test_get_company_specific_api_for_existent_company(
    api_client,
    create_num_of_companies_from_factories_without_products
):
    # given unauthed client and two companies in db
    client = api_client
    company = create_num_of_companies_from_factories_without_products(1)[0]
    # when accessing one of them with their id
    url = reverse(
        'company_details',
        kwargs={
            'company_id': company.id
        }
    )
    response = client.get(url)
    # then expecting to get data of available company
    assert response.status_code == 200
    assert response.data['name'] == company.name
    assert response.data['description'] == company.description
    assert response.data['schedule_start'] == company.schedule_start
    assert response.data['schedule_end'] == company.schedule_end
    assert response.data['schedule_weekdays'] == company.schedule_weekdays
    assert response.data['phone_number'] == company.phone_number
    assert response.data['email'] == company.email
    assert response.data['map_link'] == company.map_link
    assert response.data['social_media1'] == company.social_media1
    assert response.data['social_media2'] == company.social_media2


@pytest.mark.django_db
def test_patch_company_specific_api(
    api_client,
    create_num_of_companies_from_factories_without_products
):
    # given unauthed client and company
    client = api_client
    company = create_num_of_companies_from_factories_without_products(1)[0]
    # when client is willing to patch existing company details
    patch_data = {
        'name': 'patched_name',
        'description': 'patched description of the company',
        'schedule_start': '08:00:00',
        'schedule_end': '00:00:00'
    }
    url = reverse(
        'company_details',
        kwargs={
            'company_id': company.id
        }
    )
    response = client.patch(
        url,
        data=json.dumps(patch_data),
        content_type='application/json'
    )
    # then expecting to get status code 200 and pathed data
    assert response.status_code == 200
    assert response.data['name'] == patch_data['name']
    assert response.data['description'] == patch_data['description']
    assert response.data['schedule_start'] == patch_data['schedule_start']
    assert response.data['schedule_end'] == patch_data['schedule_end']


@pytest.mark.django_db
def test_put_company_specific_api(
    api_client,
    create_num_of_companies_from_factories_without_products,
    company_create_data_dict
):
    # given unauthed client and company
    client = api_client
    company = create_num_of_companies_from_factories_without_products(1)[0]
    capito_put_data = company_create_data_dict
    # when client is willing to put existing company details with other company details
    url = reverse(
        'company_details',
        kwargs={
            'company_id': company.id
        }
    )
    response = client.put(
        url,
        data=json.dumps(capito_put_data),
        content_type='application/json'
    )
    # then expecting to get status code 200 and other company details
    assert response.status_code == 200
    assert response.data['name'] == capito_put_data['name']
    assert response.data['description'] == capito_put_data['description']
    assert response.data['schedule_start'] == capito_put_data['schedule_start']
    assert response.data['schedule_end'] == capito_put_data['schedule_end']
    assert response.data['phone_number'] == capito_put_data['phone_number']
    assert response.data['email'] == capito_put_data['email']
    assert response.data['map_link'] == capito_put_data['map_link']
    assert response.data['social_media1'] == capito_put_data['social_media1']
    assert response.data['social_media2'] == capito_put_data['social_media2']


@pytest.mark.django_db
def test_delete_company_specific_api(
    api_client,
    create_num_of_companies_from_factories_without_products
):
    # given unauthed client and company
    client = api_client
    company = create_num_of_companies_from_factories_without_products(1)[0]
    # when trying to delete existing company
    url = reverse(
        'company_details',
        kwargs={
            'company_id': company.id
        }
    )
    response = client.delete(url)
    # then expecting status code 204 and None/null in response
    assert response.status_code == 204
    assert response.data == None
