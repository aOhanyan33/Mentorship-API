import requests
import logging
import data
import json
import test_post_get_access_token

logging.basicConfig(filename="logFileApi.log", encoding='utf-8', format='%(asctime)s: - %(levelname)s:%(message)s', level=logging.ERROR)

def test_get_groupID():
    
    try:
        baseURL = data.baseurl
        api_url = f"https://{baseURL}/api/group"
        accessToken = test_post_get_access_token.test_getToken()
        headers = {"Authorization": f"Bearer {accessToken}"}
        response =  requests.get(api_url, headers = headers)
        #print (response.json())
       
        mylist = []
        for i in response.json():
            if i['name'] == data.data_post_groupname['name']: #i['name'] == data.data_post_groupname['name']:
                mylist.append(i['groupId'])
                #print (i)
        return(mylist)
                
                       
        assert int(response.status_code) == 200
        print("The API get is passed")

    except Exception as e:
        logging.error(e)
        print(e)
        print("The request is failed")

print(test_get_groupID())
