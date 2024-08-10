from utils.apiServerUtils import getApiData
from utils.config_parser import getFlaskAppBaseURL
import pytest

baseURL = getFlaskAppBaseURL()
urlURL = 'allusercount'


# curl http://192.168.29.14:5000/api/allusercount/ -H "Accept: application/json" -i -v
# testing api all users count for status 200

@pytest.fixture()
def setup_response():
    url = baseURL + urlURL
    headers = {'Accept': 'application/json'}
    response = getApiData(url, headers)
    return response


def test_getAllUserCountStatus200():
    url = baseURL + urlURL
    headers = {'Accept': 'application/json'}
    response = getApiData(url, headers)
    assert response.status_code == 200


def test_getAllUserCountStatus406():
    url = baseURL + urlURL
    response = getApiData(url)
    assert response.status_code == 406


def test_getAllUserCountBody(setup_response):
    data = setup_response.json()
    print(data)
    assert data['count'] == 4
    assert data['status']['message'] == 'success'
    assert data['status']['status'] == 200


def test_getAllUserCountTimeTaken(setup_response):
    print(setup_response.elapsed.total_seconds())
    assert setup_response.elapsed.total_seconds() < 1
