#!/usr/bin/env python3
from http.client import responses

from testBase import TestBase

USERDETAILS = {
    "id": 6212,
    "username": "cbauser",
    "firstName": "Ryan",
    "lastName": "Rames",
    "email": "ryan.rames@gmail.com",
    "password": "cbaUser@121",
    "phone": "0412909121",
    "userStatus": 1
}
UPDATEUSER = {
    "id": 6212,
    "username": "cbauser",
    "firstName": "Ryan",
    "lastName": "Rames",
    "email": "ryan.rames@gmail.com",
    "password": "cbaUser@121",
    "phone": "0412707212",
    "userStatus": 1
}

class TestUserDetails(TestBase):
    def __init__(self):
        super().__init__()

    def testCreateUser(self):
        response = self.rest.addUser(userData=USERDETAILS)
        if response[0] == 200 and response[1]['message'] == f"{USERDETAILS['id']}":
            self.log.info('User creation successful')
            return True
        self.log.error('USer creation failed')
        return False

    def testGetUser(self):
        response = self.rest.getUserDetails(USERDETAILS['username'])
        if response[0] == 200 and response[1]['username'] == USERDETAILS['username']:
            self.log.info('Get user details successful')
            return True
        self.log.error('Get user details failed')
        return False

    def updateUserDetails(self):
        response = self.rest.udpateUserDetails(UPDATEUSER)
        if response[0] == 200 and response[1]['message'] == f"{USERDETAILS['id']}":
            responseNew = self.rest.getUserDetails(USERDETAILS['username'])
            if responseNew[0] == 200 and responseNew[1] == UPDATEUSER:
                self.log.info('Update user details successful')
                return True
        self.log.error('Update user details failed')
        return False

    def testUserLogin(self):
        response = self.rest.userLogin(USERDETAILS['username'], USERDETAILS['password'])
        if response[0] == 200 and 'logged in user' in response[1]['message']:
            self.log.info('user login successful')
            return True
        self.log.error('User login failed')
        return False

    def testUserLogout(self):
        response = self.rest.userLogout()
        if response[0] == 200 and response[1]['message'] == 'ok':
            self.log.info('user logout successful')
            return True
        self.log.error('User logout failed')
        return False

    def testInvalidUserLogin(self):
        response = self.rest.userLogin('invalidusername', 'invaliduserpassword')
        if response[0] == 400:
            self.log.info('Invalid user login failed')
            return True
        self.log.error('Invalid user login worked')
        return False

    def testDeleteUser(self):
        response = self.rest.deleteUser(USERDETAILS['username'])
        if response[0] == 200 and response[1]["message"] == f"{USERDETAILS['username']}":
            self.log.info('User deletion successful')
            return True
        self.log.error('User deletion failed')
        return False

    def testDeleteInvalidUser(self):
        response = self.rest.deleteUser('invalidusername')
        if response[0] == 404:
            self.log.info('Invalid username error')
            return True
        self.log.error('Invalid username accepted')
        return False


    def setup(self):
        super().setup()

    def run(self):
        super().run()
        if self.testCreateUser() != True:
            self.log.error('Test user creation failed')
            self.recordFailure()
        else:
            self.recordSuccess()
        if self.testGetUser() != True:
            self.log.error('Test get user failed')
            self.recordFailure()
        else:
            self.recordSuccess()
        if self.updateUserDetails() != True:
            self.log.error('Test update user details failed')
            self.recordFailure()
        else:
            self.recordSuccess()
        if self.testUserLogin() != True:
            self.log.error('Test user login failed')
            self.recordFailure()
        else:
            self.recordSuccess()
        if self.testUserLogout() != True:
            self.log.error('Test user logout failed')
            self.recordFailure()
        else:
            self.recordSuccess()
        if self.testInvalidUserLogin() != True:
            self.log.error('Test invalid user login failed')
            self.recordFailure()
        else:
            self.recordSuccess()
        if self.testDeleteUser() != True:
            self.log.error('Test delete user failed')
            self.recordFailure()
        else:
            self.recordSuccess()
        if self.testDeleteInvalidUser() != True:
            self.log.error('Test invalid username deletion failed')
            self.recordFailure()
        else:
            self.recordSuccess()


    def tearDown(self):
        super().tearDown()

if __name__ == "__main__":
    test1 = TestUserDetails()
    test1.setup()
    test1.run()
    test1.tearDown()
