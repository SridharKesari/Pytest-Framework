from utils.apiServerUtils import postAPIData
from utils.fileUtils import getJsonFromFile
from utils.config_parser import getFlaskAppBaseURL

baseURI = getFlaskAppBaseURL()
urlPath = 'register'
registerjsonFile = 'registerApiValid.json'


# testing register API with body from file
def test_registerAPI():
    url = baseURI + urlPath
    payload = getJsonFromFile(registerjsonFile)
    response = postAPIData(url, payload)
    print(response.json())
    assert response.status_code == 201
