import pytest

from utils.fileUtils import getCsvDataAsDict, getDataAsTuple
from utils.apiServerUtils import postAPIData
from utils.config_parser import getFlaskAppBaseURL

baseURI = getFlaskAppBaseURL()
dataFile = 'registerApiData.csv'
urlPath = 'register'
dataCsvFileWithStatus = 'registerApiDataWithStatus.csv'


# datadriven test from datafile, inserting all data in single test
# create multiple users in the DB, credentials mentioned in csv file
def test_dataDrivenRegisterAPI():
    url = baseURI + urlPath
    print('\nURL:', url)
    payloadList = getCsvDataAsDict(dataFile)
    for dataLines in payloadList:
        print(dataLines)
        response = postAPIData(url, dataLines)
        assert response.status_code == 201
        data = response.json()
        print(data)
        assert data['id']


# test_dataDrivenCSV.py::test_dataDrivenRegisterAPI
#
# ============================== 1 passed in 7.48s ==============================
# PASSED                 [100%]
# URL: http://127.0.0.1:5000/api/register
# {'email': 'auto6@auto', 'password': '1234'}
#
# Request URL:  http://127.0.0.1:5000/api/register
#
# Request Body:  {"email": "auto6@auto", "password": "1234"}
# {'email': 'auto6@auto', 'id': '12'}
# {'email': 'auto7@auto', 'password': '1234'}
#
# Request URL:  http://127.0.0.1:5000/api/register
#
# Request Body:  {"email": "auto7@auto", "password": "1234"}
# {'email': 'auto7@auto', 'id': '13'}
# {'email': 'auto8@auto', 'password': '1234'}
#
# Request URL:  http://127.0.0.1:5000/api/register
#
# Request Body:  {"email": "auto8@auto", "password": "1234"}
# {'email': 'auto8@auto', 'id': '14'}
# {'email': 'auto9@auto', 'password': '1234'}
#
# Request URL:  http://127.0.0.1:5000/api/register
#
# Request Body:  {"email": "auto9@auto", "password": "1234"}
# {'email': 'auto9@auto', 'id': '15'}
# {'email': 'auto10@auto', 'password': '1234'}
#
# Request URL:  http://127.0.0.1:5000/api/register
#
# Request Body:  {"email": "auto10@auto", "password": "1234"}
# {'email': 'auto10@auto', 'id': '16'}
#
# Process finished with exit code 0

# ---------------


getData = getDataAsTuple(dataCsvFileWithStatus)


# datadriven test from datafile, used pytest parameterization, separate test for each from data file
@pytest.mark.parametrize('input, respStatus', getData)
def test_dataDrivenParametrized(input, respStatus):
    url = baseURI + urlPath
    keys = ['email', 'password']
    requestDict = dict(zip(keys, input))
    print('Request Dict:', requestDict, respStatus)
    response = postAPIData(url, requestDict)
    assert response.status_code == int(respStatus)
