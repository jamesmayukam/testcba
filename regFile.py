import unittest
from testPet import TestPetDetails
from testStore import TestStoreDetails
from testUser import TestUserDetails

class TestPet(unittest.TestCase):

    petInstance = TestPetDetails()
    storeInstance = TestStoreDetails()
    userInstance = TestUserDetails()

    def test_testCreatePet(self):
        self.assertEqual(self.petInstance.testCreatePet(), True)

    def test_testPetFetch(self):
        self.assertEqual(self.petInstance.testPetFetch(), True)

    def test_testPetFetchWrongId(self):
        self.assertEqual(self.petInstance.testPetFetchWrongId(), True)

    def test_testPetDeletion(self):
        self.assertEqual(self.petInstance.testPetDeletion(), True)

    def test_testCreateStoreOrder(self):
        self.assertEqual(self.storeInstance.testCreateStoreOrder(), True)

    def test_testGetStoreOrder(self):
        self.assertEqual(self.storeInstance.testGetStoreOrder(), True)

    def test_testGetStoreInventory(self):
        self.assertEqual(self.storeInstance.testGetStoreInventory(), True)

    def test_testDeleteStoreOrder(self):
        self.assertEqual(self.storeInstance.testDeleteStoreOrder(), True)







    def test_testCreateUser(self):
        self.assertEqual(self.userInstance.testCreateUser(), True)

    def test_testGetUser(self):
        self.assertEqual(self.userInstance.testGetUser(), True)

    def test_updateUserDetails(self):
        self.assertEqual(self.userInstance.updateUserDetails(), True)

    def test_testUserLogin(self):
        self.assertEqual(self.userInstance.testUserLogin(), True)

    def test_testUserLogout(self):
        self.assertEqual(self.userInstance.testUserLogout(), True)

    def test_testInvalidUserLogin(self):
        self.assertEqual(self.userInstance.testInvalidUserLogin(), True)

    def test_testDeleteUser(self):
        self.assertEqual(self.userInstance.testDeleteUser(), True)

    def test_testDeleteInvalidUser(self):
        self.assertEqual(self.userInstance.testDeleteInvalidUser(), True)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestPet('test_testCreatePet'))
    suite.addTest(TestPet('test_testPetFetch'))
    suite.addTest(TestPet('test_testPetFetchWrongId'))
    suite.addTest(TestPet('test_testPetDeletion'))


    suite.addTest(TestPet('test_testCreateStoreOrder'))
    suite.addTest(TestPet('test_testGetStoreOrder'))
    suite.addTest(TestPet('test_testGetStoreInventory'))
    suite.addTest(TestPet('test_testDeleteStoreOrder'))

    suite.addTest(TestPet('test_testCreateUser'))
    suite.addTest(TestPet('test_testGetUser'))
    suite.addTest(TestPet('test_updateUserDetails'))
    suite.addTest(TestPet('test_testUserLogin'))
    suite.addTest(TestPet('test_testUserLogout'))
    suite.addTest(TestPet('test_testInvalidUserLogin'))
    suite.addTest(TestPet('test_testDeleteUser'))
    suite.addTest(TestPet('test_testDeleteInvalidUser'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
