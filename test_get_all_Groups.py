import requests
import logging
import data
import json
import test_post_get_access_token

logging.basicConfig(filename="logFileApi.log", encoding='utf-8', format='%(asctime)s: - %(levelname)s:%(message)s', level=logging.ERROR)

def test_get_all_groups():
    
    try:
        baseURL = data.baseurl
        api_url = f"https://{baseURL}/api/group"
        accessToken = test_post_get_access_token.test_getToken()
        headers = {"Authorization": f"Bearer {accessToken}"}
        response =  requests.get(api_url, headers = headers)

        print(response.text)
        
        assert int(response.status_code) == 200
        print("The API get of All Groups is passed")

    except Exception as e:
        logging.error(e)
        print("The request is failed")

test_get_all_groups()

        