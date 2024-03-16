import pytest
from rest_framework.reverse import reverse


@pytest.mark.django_db
def test_company_list_api(
    api_client
):
    # given unauthorized client and empty db
    client = api_client
    # when client accessing the companys list endpoint
    url = reverse('companies')
    response = client.get(url)
    # then expecting empty list and status 200
    print(response.content.decode('utf-8'))
    assert response.status_code == 200
    assert response.data['results'] == []
