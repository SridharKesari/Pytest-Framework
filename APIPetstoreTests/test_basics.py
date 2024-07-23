import requests, json

baseURI = 'https://petstore.swagger.io/v2/pet/'
petID = '151'


# GET API
# test valid response or response is not empty
def test_getPetById_response():
    url = baseURI + petID
    header = {'Content-Type': 'application/json'}  # required during POST
    print('RequestURL:', url)
    response = requests.get(url, verify=False, headers=header)
    data = response.json()
    print(json.dumps(data, indent=4))  # print(data)
    assert len(data) > 0, 'Empty Response'


# testing response body for ID key
def test_getPetById_id():
    url = baseURI + petID
    header = {'Content-Type': 'application/json'}  # required during POST
    print('RequestURL:', url)
    response = requests.get(url, verify=False, headers=header)
    data = response.json()
    assert data['id'] == 151
    assert data['name'] == 'doggie'
