import requests
import logging
import data
import json
#import test_post_get_access_token

logging.basicConfig(filename="logFileApi.log", encoding='utf-8', format='%(asctime)s: - %(levelname)s:%(message)s', level=logging.ERROR)

     #-- Get token-- #
def test_getToken():

    try:
        baseURL = data.baseurl
        api_url = f"https://{baseURL}/api/auth/token"
        todo = data.data_post_credentials
        response = requests.post(api_url, json=todo)

        assert int(response.status_code) == 200
        print("The API post to get token is passed")
    
    except Exception as e:
        logging.error(e)
        print("The request is failed")

    finally:
        json_response = json.loads(response.text)
        access_token = json_response["accessToken"]
    
    return access_token

     # -- Create Group--#
def test_post_create_group():
    try:
        baseURL = data.baseurl
        api_url = f"https://{baseURL}/api/group"
        todo = data.data_post_groupname
        accessToken = test_getToken()
        headers = {"Authorization": f"Bearer {accessToken}"}
        response = requests.post(api_url, json=todo, headers=headers)
        print(response.text)

        assert int(response.status_code) == 200
        print("The API post of creating group is passed")

    except Exception as e:
        logging.error(e)
        print("The request is failed")

    finally:
        api_url = f"https://{baseURL}/api/group"
        response =  requests.get(api_url, headers = headers)
        print(response.text)

        
     # -- Get All Groups --#
def test_get_all_groups():
    
    try:
        baseURL = data.baseurl
        api_url = f"https://{baseURL}/api/group"
        accessToken = test_getToken()
        headers = {"Authorization": f"Bearer {accessToken}"}
        response =  requests.get(api_url, headers = headers)

        print(response.text)
        
        assert int(response.status_code) == 200
        print("The API get of All Groups is passed")

    except Exception as e:
        logging.error(e)
        print("The request is failed")

    # -- Get Group ID --#
def test_get_groupID():
    
    try:
        baseURL = data.baseurl
        api_url = f"https://{baseURL}/api/group"
        accessToken = test_getToken()
        headers = {"Authorization": f"Bearer {accessToken}"}
        response =  requests.get(api_url, headers = headers)
        #print (response.json())
       
        mylistCreated = []
        for i in response.json():
            if i['name'] == data.data_post_groupname['name']: 
                mylistCreated.append(i['groupId']) 
                #print (i)
        return(mylistCreated)
                
                       
        assert int(response.status_code) == 200
        print("The API get is passed")

    except Exception as e:
        logging.error(e)
        print(e)
        print("The request is failed")
     
     #-- Update Group--#
def test_update_createdGroup():
    try:
        groupIdList = test_get_groupID()
        accessToken = test_getToken()
        baseURL = data.baseurl
        api_url2 = f"https://{baseURL}/api/group"
        headers = {"Authorization": f"Bearer {accessToken}"}
        
        
        for groupId in groupIdList:
            api_url1 = f"https://{baseURL}/api/group/{groupId}"
            todo = data.data_put
            response1 = requests.put(api_url1, headers = headers,json=todo)       
       
        response2 =  requests.get(api_url2, headers = headers)
        mylistUpdated = []
        for i in response2.json():
            if i['name'] == data.data_put['name']: 
                mylistUpdated.append(i['groupId'])
                #print (i)
        return mylistUpdated
                    
        assert int(response1.status_code) == 200
        print("The API put is passed")
            
    except Exception as e:
        logging.error(e)
        print("The put request is failed")

     #-- Create and Delete Group--#
def test_delete_Group():
    
    try:
        test_post_create_group() #-- Create Group--#
        groupCreated = test_get_groupID()
        groupIdListUpdated = test_update_createdGroup() 
        accessToken = test_getToken()
        print ("Created list =", groupCreated)
        print("Updated list = ", groupIdListUpdated)
        
        for groupId in groupIdListUpdated:
            baseURL = data.baseurl
            api_url = f"https://{baseURL}/api/group/{groupId}"
            headers = {"Authorization": f"Bearer {accessToken}"}
            response = requests.delete(api_url, headers = headers)
        
        assert int(response.status_code) == 200
        print("The API delete is passed")
    
    except Exception as e:
        logging.error(e)
        print("The Delete group request is failed")



#test_post_create_group()
#print(test_get_groupID())
#print(test_update_createdGroup())
test_delete_Group()

