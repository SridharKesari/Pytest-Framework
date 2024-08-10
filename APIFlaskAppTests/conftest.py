import pytest

from utils.fileUtils import getJsonFromFile
from utils.apiServerUtils import postAPIData, getApiData
# post is for login and get is to get the users api
from utils.config_parser import getFlaskAppBaseURL

loginJsonFile = 'loginValid.json'
baseURI = getFlaskAppBaseURL()
loginURLPath = 'login'


@pytest.fixture
def get_token():
    loginURL = baseURI + loginURLPath
    payload = getJsonFromFile(loginJsonFile)
    resp = postAPIData(loginURL, payload)
    print(resp.json()['token'])
    token = resp.json()['token']
    yield token
