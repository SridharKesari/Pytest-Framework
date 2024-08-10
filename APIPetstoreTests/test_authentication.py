import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

url = 'https://httpbin.org/digest-auth/auth/123/123/MD5'
auth = HTTPDigestAuth('123', '123')

def test_basicAuth():
    headers = {'Accept': 'application/json'}
    r = requests.get(url, auth=auth, verify=False)
    print(r.status_code)