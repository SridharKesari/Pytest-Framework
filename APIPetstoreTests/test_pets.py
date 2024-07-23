from utils.libutils import getAPIData
from utils.config_parser import getPetAPIURL

# baseURI = 'https://petstore.swagger.io/v2/pet/'
petID = '191'
baseURI = getPetAPIURL()  # use config parser to get the URL from the pets_qa.ini config file


def test_getPetById_response():
    url = baseURI + petID
    data, resp_status, timeTaken = getAPIData(url)
    assert data['id'] == int(petID)
    assert resp_status == 200
    print(f'Time Taken: {timeTaken}')
