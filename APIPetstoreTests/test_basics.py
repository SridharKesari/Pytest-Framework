import json
import requests

baseURI = 'https://petstore.swagger.io/v2/pet/'
petID = '191'


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


# testing response body for 'ID' key
def test_getPetById_id():
    url = baseURI + petID
    header = {'Content-Type': 'application/json'}  # required during POST
    print('RequestURL:', url)
    response = requests.get(url, verify=False, headers=header)
    data = response.json()
    assert data['id'] == int(petID)
    assert data['name'] == 'Cutie'


# POST API
# test adding new pet to store
def test_addNewPet():
    url = baseURI
    header = {'Content-Type': 'application/json'}
    payload = {'id': 191, 'name': 'Cutie', 'status': 'available'}
    response = requests.post(url, verify=False, json=payload, headers=header)
    data = response.json()
    assert data['id'] == 191
    assert len(data) > 0
    print(data)
