import json
import requests


# get API call and return response data
def getAPIData(url):
    header = {'Content-Type': 'application/json'}
    print('RequestURL:', url)
    response = requests.get(url, verify=False, headers=header)
    data = response.json()
    assert len(data) > 0, 'Empty Response'
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken


def postAPIData(url, petID, name, status):
    header = {'Content-Type': 'application/json'}
    payload = {'id': petID, 'name': name, 'status': status}
    response = requests.post(url, verify=False, json=payload, headers=header)
    data = response.json()
    assert len(data) > 0
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken
