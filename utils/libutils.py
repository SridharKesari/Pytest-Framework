import json

import allure
import requests


# get API call and return response data
def getAPIData(url):
    header = {'Content-Type': 'application/json'}
    print('RequestURL for get:', url)
    response = requests.get(url, verify=False, headers=header)
    data = response.json()
    assert len(data) > 0, 'Empty Response'
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken


# post API call
def postAPIData(url, petID, name, status):
    header = {'Content-Type': 'application/json'}
    print('RequestURL for post:', url)
    payload = {'id': petID, 'name': name, 'status': status}
    response = requests.post(url, verify=False, json=payload, headers=header)
    data = response.json()
    assert len(data) > 0
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken


@allure.step('Doing Put Data')
# put API call
def putAPIData(url, body):
    header = {'Content-Type': 'application/json'}
    print('RequestURL for put:', url)
    print('ReqBody: ', json.dumps(body))
    response = requests.put(url, verify=False, json=body, headers=header)
    data = response.json()
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken


# delete API call
def deleteAPIData(url, opHeader=None):
    header = {'Content-Type': 'application/json'}
    print('RequestURL for delete:', url)
    header = (header | opHeader) if isinstance(opHeader, dict) else header
    response = requests.delete(url, verify=False, headers=header)
    print(response.request.headers)
    data = response.json()
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken
