from utils.libutils import getAPIData

baseURI = 'https://petstore.swagger.io/v2/pet/'
petID = '191'


def test_getPetById_response():
    url = baseURI + petID
    data, resp_status, timeTaken = getAPIData(url)
    assert data['id'] == int(petID)
    assert resp_status == 200
    print(f'Time Taken: {timeTaken}')
