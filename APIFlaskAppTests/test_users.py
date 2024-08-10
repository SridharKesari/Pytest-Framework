import json

import pytest

from utils.fileUtils import getJsonFromFile
from utils.apiServerUtils import postAPIData, getApiData
# post is for login and get is to get the users api
from utils.config_parser import getFlaskAppBaseURL

# loginJsonFile = 'loginValid.json'
baseURI = getFlaskAppBaseURL()
# loginURLPath = 'login'
usersURLPath = 'users'


# @pytest.fixture
# def get_token():
#     loginURL = baseURI + loginURLPath
#     payload = getJsonFromFile(loginJsonFile)
#     resp = postAPIData(loginURL, payload)
#     print(resp.json()['token'])
#     token = resp.json()['token']
#     yield token


# test get users with fixtures
def test_getUsers(get_token):
    token = get_token
    usersURL = baseURI + usersURLPath
    headers = {'x-access-token': token}
    resp_users = getApiData(usersURL, headers)
    print(resp_users.json())
    print(json.dumps(resp_users.json(), indent=4))
    assert resp_users.json()['users'][0]['email'] == 'admin@admin'
