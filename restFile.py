#!/usr/bin/env python3
import requests
from requests import Timeout, RequestException

## Base Class for REST API.
# This has the methods and properties for the RESTful API
class RestBase(object):
    def __init__(self):
        self._baseUrl = 'https://petstore.swagger.io/v2'
        self._headers = {'Accept': 'application/json'}

    ## Method to send GET, PUT, POST and DELETE requests to RESTful API server
    # Returns a tuple of status code and response body
    def _sendRequest(self, api, requestType='GET', params=None, json=None, data=None):
        url = f'{self._baseUrl}{api}'
        try:
            if requestType == 'GET':
                response = requests.get(url=url, headers=self._headers, params=params)
            elif requestType == 'PUT':
                response = requests.put(url=url, headers=self._headers, json=json)
            elif requestType == 'POST':
                if json:
                    response = requests.post(url=url, headers=self._headers, json=json)
                elif data:
                    response = requests.post(url=url, headers=self._headers, data=data)
            elif requestType == 'DELETE':
                response = requests.delete(url=url, headers=self._headers)
            else:
                raise Exception('Invalid Method')
            '''print(f"$$$$$$$$$$$$$$ {response}")
            print(f"$$$$$$$$$$$ {response.url}")
            print(f"$$$$$$$$$$$$$ {response.text}")'''
        except Timeout as t:
            print(f"The request timed out - {t}")
            return None
        except RequestException as re:
            print(f"Request Exception occurred - {re}")
            return None
        except Exception as e:
            print(f"Exception occurred - {e}")
            return None
        #print(f"@@@@@@@@@@@@@ {response.status_code}")
        if response.text != '':
            #print(f"############# {response.json()}")
            return (response.status_code, response.json())
        return (response.status_code, response.text)

    ## Method to get pet details
    def getPetDetails(self, petId):
        assert type(petId) is int, 'PETID must be an integer'
        return self._sendRequest(f"/pet/{petId}", requestType='GET')

    ## Method to get pet details by status
    def getPetDetailsByStatus(self, status):
        assert status in ['available', 'pending', 'sold'], \
            'Status must be available/pending/sold'
        params = {'status': status}
        return self._sendRequest(f"/pet/findByStatus", requestType='GET', params=params)

    ## Method to add pet to the server
    def addPet(self, petData):
        assert petData != None, 'Pet details mandatory'
        return self._sendRequest('/pet', requestType='POST', json=petData)

    ## Method to modify the existing pet record
    def modifyPet(self, petData):
        assert petData != None, 'Pet details mandatory'
        return self._sendRequest('/pet', requestType='PUT', json=petData)

    ## Method to modify the existing pet using form
    def modifyPetByForm(self, petData):
        assert petData != None, 'Pet details mandatory'
        return self._sendRequest(f"/pet/{petData['petId']}", requestType='POST', data=petData)

    ## Method to delete the existing pet record
    def deletePet(self, petId):
        assert petId != None, 'Pet ID mandatory'
        return self._sendRequest(f'/pet/{petId}', requestType='DELETE')

    def getStoreInventory(self):
        return self._sendRequest(f"/store/inventory", requestType='GET')

    def getStoreOrder(self, orderId):
        assert orderId != None, 'Order ID mandatory'
        return self._sendRequest(f"/store/order/{orderId}", requestType='GET')

    def createStoreOrder(self, orderData):
        assert orderData != None, 'Order Data mandatory'
        return self._sendRequest('/store/order', requestType='POST', json=orderData)

    def deleteStoreOrder(self, orderId):
        assert orderId != None, 'Order ID mandatory'
        return self._sendRequest(f'/store/order/{orderId}', requestType='DELETE')


    ##############

    def addUser(self, userData):
        assert userData != None, 'USer Data mandatory'
        return self._sendRequest('/user', requestType='POST', json=userData)

    #getUserDetails(USERDETAILS['id'])
    def getUserDetails(self, userName):
        assert userName != None, 'Username mandatory'
        return self._sendRequest(f"/user/{userName}", requestType='GET')

    def udpateUserDetails(self, userData):
        assert userData != None, 'Updated user details mandatory'
        return self._sendRequest(f"/user/{userData['username']}", requestType='PUT', json=userData)

    def deleteUser(self, userName):
        assert userName != None, 'Username mandatory'
        return self._sendRequest(f'/user/{userName}', requestType='DELETE')

    def userLogin(self, username, password):
        assert username != None and password != None, 'Username and password mandatory'
        data = {'username': username, 'password': password}
        return self._sendRequest(f'/user/login', requestType='GET', params=data)

    def userLogout(self):
        return self._sendRequest(f'/user/logout', requestType='GET')






