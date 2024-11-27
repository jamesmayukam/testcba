#!/usr/bin/env python3

from testBase import TestBase

PETDETAILS = {
        "id": 6007,
        "name": "Dogie6003",
        "category": {
            "id": 6,
            "name": "Dogs6"
        },
        "photoUrls": ["http://example.com/Dog6005-1.jpg"],
        "tags": [{"id": 6, "name": "white"}],
        "status": "pending"
    }
class TestPetDetails(TestBase):
    def __init__(self):
        super().__init__()

    def testCreatePet(self):
        response = self.rest.addPet(petData=PETDETAILS)
        if response[0] == 200 and response[1]['id'] == PETDETAILS['id']:
            self.log.info('Pet creation successful')
            return True
        self.log.error('Pet creation failed')
        return False

    def testPetFetch(self):
        response = self.rest.getPetDetails(PETDETAILS['id'])
        if response[0] == 200 and response[1]['id'] == PETDETAILS['id']:
            self.log.info('Pet details fetch successful')
            return True
        self.log.error('Failed to get pet details')
        return False

    def testPetFetchWrongId(self):
        response = self.rest.getPetDetails(99911122)
        if response[0] == 404:
            self.log.info('Pet fetch with wrong ID test Successful')
            return True
        self.log.error('Pet fetch with wrong ID test Failed')
        return False

    def testPetDeletion(self):
        response = self.rest.deletePet(PETDETAILS['id'])
        if response[0] == 200 and response[1]["message"] == f"{PETDETAILS['id']}":
            self.log.info('Pet deletion successful')
            return True
        self.log.error('Pet deletion failed')
        return False

    def setup(self):
        super().setup()

    def run(self):
        super().run()
        if self.testCreatePet() != True:
            self.log.error('Test pet creation failed')
            self.recordFailure()
        else:
            self.recordSuccess()
        if self.testPetFetch() != True:
            self.log.error('Test pet fetch failed')
            self.recordFailure()
        else:
            self.recordSuccess()
        if self.testPetFetchWrongId() != True:
            self.log.error('Test pet fetch with wrong ID failed')
            self.recordFailure()
        else:
            self.recordSuccess()
        if self.testPetDeletion() != True:
            self.log.error('Test pet deletion failed')
            self.recordFailure()
        else:
            self.recordSuccess()

    def tearDown(self):
        super().tearDown()

if __name__ == "__main__":
    test1 = TestPetDetails()
    test1.setup()
    test1.run()
    test1.tearDown()
