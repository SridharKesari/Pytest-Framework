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
