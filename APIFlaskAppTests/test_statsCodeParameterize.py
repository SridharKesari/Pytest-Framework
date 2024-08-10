from utils.apiServerUtils import getApiData
from utils.config_parser import getFlaskAppBaseURL
import pytest

baseURL = getFlaskAppBaseURL()
urlURL = 'allusercount'

testData = [  # list of tuples
    ('application/json', 200),
    ('application/xml', 406),
    ('multipart/mixed', 406),
    ('text/html', 200)
]


@pytest.mark.parametrize('type, status', testData)
def test_getAllUserCountStatus(type, status):
    url = baseURL + urlURL
    headers = {'Accept': type}
    response = getApiData(url, headers)
    print(response.status_code)
    assert response.status_code == status
