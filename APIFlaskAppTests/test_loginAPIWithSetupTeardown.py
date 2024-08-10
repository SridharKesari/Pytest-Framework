import random
import time

import pytest
from utils.apiServerUtils import postAPIData, delAPIData
from utils.fileUtils import getJsonFromFile
from utils.config_parser import getFlaskAppBaseURL

baseURL = getFlaskAppBaseURL()
regURLPath = 'register'
loginUrlPath = 'login'
deleteUrlPath = 'delete'
registerJsonFile = 'registerApiValid.json'
randNum = random.randint(0, 1000)
email = 'automateUser@auto' + str(randNum)
password = '12345'


@pytest.fixture()  # (scope='module')
def reg_user():
    # setup starts
    payLoad = getPayloadDict_RegAPI(email, password)
    regUrl = baseURL + regURLPath
    reg_response = postAPIData(regUrl, payLoad)  # register a user
    assert reg_response.status_code == 201
    assert reg_response.json()['id']
    data = reg_response.json()
    print('Data to be yield: ', data)
    print("one - Inside fixture SETUP")
    yield data  # anything after this stmt, will run as part of teardown or after the test function is executed.
    # teardown starts
    time.sleep(5)
    print("three - Inside fixture YIELD")
    delUrl = baseURL + deleteUrlPath
    loginUrl = baseURL + loginUrlPath
    login_resp = postAPIData(loginUrl, payLoad)
    token = login_resp.json()['token']
    headers = {'x-access-token': token}
    payLoad = {'id': reg_response.json()['id']}
    del_resp = delAPIData(delUrl, payLoad, headers)
    print('Delete status code: ', del_resp)
    assert del_resp.status_code == 200
    assert del_resp.json()['id'] == reg_response.json()['id']


def test_loginCorrectCreds(reg_user):
    loginData = reg_user
    print('LoginData: ', loginData)
    payLoad = getPayloadDict_RegAPI(email, password)
    loginUrl = baseURL + loginUrlPath
    login_response = postAPIData(loginUrl, payLoad)  # login a user
    print('login_response: ', login_response.json())
    assert login_response.status_code == 200
    print("two")


def test_loginEmptyPassword(reg_user):
    regUserData = reg_user
    print('Register User: ', regUserData)
    payLoad = getPayloadDict_RegAPI(email, '')
    loginUrl = baseURL + loginUrlPath
    login_response = postAPIData(loginUrl, payLoad)
    assert login_response.status_code == 401


def getPayloadDict_RegAPI(email=None, pwd=None):
    payload = getJsonFromFile(registerJsonFile)
    payload['email'] = email  # get the values mentioned in the beginning
    payload['password'] = pwd
    return payload
