import requests
import logging
import data
import json

logging.basicConfig(filename="logFileApi.log", encoding='utf-8', format='%(asctime)s: - %(levelname)s:%(message)s', level=logging.ERROR)

def test_getToken():

    try:
        baseURL = data.baseurl
        api_url = f"https://{baseURL}/api/auth/token"
        todo = data.data_post_credentials
        response = requests.post(api_url, json=todo)
        #print(response.text)

        assert int(response.status_code) == 200
        print("The API post to get token is passed")
    
    except Exception as e:
        logging.error(e)
        print("The request is failed")

    finally:
        json_response = json.loads(response.text)
        access_token = json_response["accessToken"]
    
    return access_token
