#!/usr/bin/env python3

from testBase import TestBase

ORDERDETAILS = {
    "id": 6101,
    "petId": 61,
    "quantity": 1,
    "shipDate": "2024-12-25T02:21:51.521Z",
    "status": "placed",
    "complete": 'true'
}
class TestStoreDetails(TestBase):
    def __init__(self):
        super().__init__()

    def testCreateStoreOrder(self):
        response = self.rest.createStoreOrder(orderData=ORDERDETAILS)
        if response[0] == 200 and response[1]['id'] == ORDERDETAILS['id']:
            self.log.info('Store order creation successful')
            return True
        self.log.error(f'status code : {response[0]} and Reason : {response[1]}')
        return False

    def testGetStoreOrder(self):
        response = self.rest.getStoreOrder(ORDERDETAILS['id'])
        if response[0] == 200 and response[1]['id'] == ORDERDETAILS['id']:
            self.log.info('Get store order successful')
            return True
        self.log.error(f'status code : {response[0]} and Reason : {response[1]}')
        return False

    def testGetStoreInventory(self):
        response = self.rest.getStoreInventory()
        if response[0] == 200:
            self.log.info('Get store inventory successful')
            return True
        self.log.error(f'status code : {response[0]} and Reason : {response[1]}')
        return False

    def testDeleteStoreOrder(self):
        response = self.rest.deleteStoreOrder(ORDERDETAILS['id'])
        if response[0] == 200 and response[1]["message"] == f"{ORDERDETAILS['id']}":
            self.log.info('Store order deletion successful')
            return True
        self.log.error(f'status code : {response[0]} and Reason : {response[1]}')
        return False

    def setup(self):
        super().setup()

    def run(self):
        super().run()
        if self.testCreateStoreOrder() != True:
            self.log.error('Test store order creation failed')
            self.recordFailure()
        else:
            self.recordSuccess()
        if self.testGetStoreOrder() != True:
            self.log.error('Test store order fetch failed')
            self.recordFailure()
        else:
            self.recordSuccess()
        if self.testGetStoreInventory() != True:
            self.log.error('Test store inventory failed')
            self.recordFailure()
        else:
            self.recordSuccess()
        if self.testDeleteStoreOrder() != True:
            self.log.error('Test store order deletion failed')
            self.recordFailure()
        else:
            self.recordSuccess()

    def tearDown(self):
        super().tearDown()

if __name__ == "__main__":
    test1 = TestStoreDetails()
    test1.setup()
    test1.run()
    test1.tearDown()
