import requests
import logging
import data
import json
import test_post_get_access_token

logging.basicConfig(filename="logFileApi.log", encoding='utf-8', format='%(asctime)s: - %(levelname)s:%(message)s', level=logging.ERROR)

def test_post_create_group():
    try:
        baseURL = data.baseurl
        api_url = f"https://{baseURL}/api/group"
        todo = data.data_post_groupname
        accessToken = test_post_get_access_token.test_getToken()
        headers = {"Authorization": f"Bearer {accessToken}"}
        response = requests.post(api_url, json=todo, headers=headers)
    

        assert int(response.status_code) == 200
        print("The API post of creating group is passed")

    except Exception as e:
        logging.error(e)
        print("The request is failed")

    # finally:
    #     response = json.loads(response.text)
    #     new_course_id = response["name"]
    
    # return new_course_id


test_post_create_group() 

