import requests
import logging
import data
import test_get_GroupID_from_all
import test_post_get_access_token

logging.basicConfig(filename="logFileApi.log", encoding='utf-8', format='%(asctime)s: - %(levelname)s:%(message)s', level=logging.ERROR)



def test_delete_Group():
    
    try:
        
        groupIdList = test_get_GroupID_from_all.test_get_groupID()
        accessToken = test_post_get_access_token.test_getToken()
        
        for groupId in groupIdList:
            baseURL = data.baseurl
            api_url = f"https://{baseURL}/api/group/{groupId}"
            headers = {"Authorization": f"Bearer {accessToken}"}
            response = requests.delete(api_url, headers = headers)
        
        assert int(response.status_code) == 200
        print("The API delete is passed")
    
    except Exception as e:
        logging.error(e)
        print("The Delete group request is failed")
     

test_delete_Group()


