import requests, json


def getApiData(url, opHeader=None):
    headers = {'Content-Type': 'application/json'}
    headers = (headers | opHeader) if isinstance(opHeader, dict) else headers
    response = requests.get(url, verify=False, headers=headers)
    print('\nRequest URL: ', url, headers)
    print('request header', response.request.headers)
    print('response header: ', response.headers)
    return response  # send full response to test, perform checks in test


def postAPIData(url, body):
    headers = {'Content-Type': 'application/json'}
    print('\nRequest URL: ', url)
    print('\nRequest Body: ', json.dumps(body))
    return requests.post(url, verify=False, json=body, headers=headers)


def delAPIData(url, body, opHeader=None):
    headers = {'Content-Type': 'application/json'}
    headers = (headers | opHeader) if isinstance(opHeader, dict) else headers
    print('\nRequest URL: ', url)
    print('\nRequest Body: ', json.dumps(body))
    response = requests.delete(url, json=body, headers=headers)
    return response