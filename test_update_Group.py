import requests
import logging
import data
import json
import test_post_get_access_token
import test_get_GroupID_from_all


logging.basicConfig(filename="logFileApi.log", encoding='utf-8', format='%(asctime)s: - %(levelname)s:%(message)s', level=logging.ERROR)


def test_update_createdGroup():
    try:
        groupIdList = test_get_GroupID_from_all.test_get_groupID()
        accessToken = test_post_get_access_token.test_getToken()
        
        for groupId in groupIdList:
            baseURL = data.baseurl
            api_url = f"https://{baseURL}/api/group/{groupId}"
            accessToken = test_post_get_access_token.test_getToken()
            headers = {"Authorization": f"Bearer {accessToken}"}
            todo = data.data_put
            response = requests.put(api_url, headers = headers,json=todo)
            print (response.text)  
              
        assert int(response.status_code) == 200
        print("The API put is passed")
            
    except Exception as e:
        logging.error(e)
        print("The put request is failed")
       
test_update_createdGroup()        