from utils.fileUtils import getJsonFromFile
from utils.apiServerUtils import postAPIData, getApiData
# post is for login and get is to get the users api
from utils.config_parser import getFlaskAppBaseURL

loginJsonFile = 'loginValid.json'
baseURI = getFlaskAppBaseURL()
loginURLPath = 'login'
usersURLPath = 'users'


# demo test with token
def test_getUsersDemo():
    # first login with and existing user
    loginURL = baseURI + loginURLPath
    payload = getJsonFromFile(loginJsonFile)
    resp = postAPIData(loginURL, payload)
    print(resp.json()['token'])
    token = resp.json()['token']
    userURL = baseURI + usersURLPath
    headers = {'x-access-token': token}
    resp_users = getApiData(userURL, headers)
    print(resp_users.json())


