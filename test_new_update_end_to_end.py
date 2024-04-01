import requests
import logging
import data
import json

logging.basicConfig(filename="logFileApi.log", encoding='utf-8', format='%(asctime)s: - %(levelname)s:%(message)s', level=logging.ERROR)

     #-- Get token-- #
#def test_getToken():

try:
    baseURL = data.baseurl
    api_url1 = f"https://{baseURL}/api/auth/token"
    todo1 = data.data_post_credentials
    todo_update = data.data_put
        
    response_token = requests.post(api_url1, json=todo1) #-- Get token-- #
    json_response = json.loads(response_token.text)
    access_token = json_response["accessToken"]
    assert  int(response_token.status_code) == 200
    print("The API get token is passed")
    
except Exception as e:
    logging.error(e)
    print("The get token request is failed")     
    
try: # -- Create Group--# 
    api_url2 = f"https://{baseURL}/api/group"
    todo2 = data.data_post_groupname
    headers = {"Authorization": f"Bearer {access_token}"}
    
    response_create = requests.post(api_url2, json=todo2, headers=headers)   
    
    assert int(response_create.status_code) == 200
    print("The API create User is passed")
    
except Exception as e:
    logging.error(e)
    print("The create User request is failed")   
    
try: # -- Get All Groups --#
    response_getAll =  requests.get(api_url2, headers = headers)
    assert int(response_getAll.status_code) == 200
    print("The API get All Group is passed")

except Exception as e:
    logging.error(e)
    print("The get All User request is failed") 

try: 
    response_getGroupID =  requests.get(api_url2, headers = headers) # -- Get Group ID --#
    for i in response_getGroupID.json():
            if i['name'] == data.data_post_groupname['name']: 
                GroupID = i['groupId']
                api_url_update = f"https://{baseURL}/api/group/{GroupID}"
                response_update = requests.put(api_url_update, headers = headers,json=todo_update)  #-- Update Group--#
                response_delete = requests.delete(api_url_update, headers = headers)                #-- Delete Group--#
    
    assert  int(response_getGroupID.status_code) == 200
    print("The API get Group ID is passed")
    
    int(response_update.status_code) == 200
    print("The API update Group name is passed")
    
    int(response_delete.status_code) == 200
    print("The API delete Group is passed")
    
    
except Exception as e:
    logging.error(e)
    print("The one of get GroupID/update/delete request is failed") 
   
  
