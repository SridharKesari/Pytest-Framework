from utils.libutils import getAPIData, postAPIData, putAPIData, deleteAPIData
from utils.config_parser import getPetAPIURL

# baseURI = 'https://petstore.swagger.io/v2/pet/'
petID = '191'
baseURI = getPetAPIURL()  # use config parser to get the URL from the pets_qa.ini config file


def test_postPetByDetails_request():
    data, resp_status, timeTaken = postAPIData(baseURI, petID, 'Cutie', 'available')
    assert data['id'] == int(petID)
    assert len(data) > 0
    print(data)
    print(f'Time Taken: {timeTaken}')


def test_getPetById_response():
    url = baseURI + petID
    data, resp_status, timeTaken = getAPIData(url)
    assert data['id'] == int(petID)
    assert resp_status == 200
    print(data)
    print(f'Time Taken: {timeTaken}')


# test updating a pet
def test_updating_pet():
    payload = {'id': int(petID), 'name': 'Sweety', 'status': 'pending'}
    data, resp_status, timeTaken = putAPIData(baseURI, payload)
    assert data['id'] == int(petID)
    print(data)
    print(f'Time Taken: {timeTaken}')


# test deleting a pet
def test_delete_pet():
    url = baseURI + petID
    apiKey = {'api_key': 'key1'}
    data, resp_status, timeTaken = deleteAPIData(url, apiKey)
    assert resp_status == 200
    assert data['message'] == petID
    print(data)
    print(f'Time Taken: {timeTaken}')
