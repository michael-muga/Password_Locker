from re import U
import unittest
from user_credentials import Usercredentials

class TestUsercredentials(unittest.TestCase):
    '''
    test class that define test cases for the usercredentials behaviours
    '''

    def setUp(self):

        self.new_credentials = Usercredentials("gmail","254mike")

    def test__init(self):

        self.assertEqual(self.new_credentials.site_name,"gmail")
        self.assertEqual(self.new_credentials.password,"254mike")

    def tearDown(self):
        '''
        teardown method that clean up after each test case has run
        '''   
        Usercredentials.user_credential_list=[]

    def test_save_credential(self):

        self.new_credentials.save_credentials()
        self.assertEqual(len(Usercredentials.user_credential_list),1)

    def test_save_multiple_credentials(self):
        self.new_credentials.save_credentials()
        test_credential = Usercredentials("twitter","787627")
        test_credential.save_credentials()
        self.assertEqual(len(Usercredentials.user_credential_list),2)

    def test_delete_credentials(self):
        '''
        test is credentials can be removed from the list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Usercredentials("twitter","787627")
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Usercredentials.user_credential_list),1)

if __name__ == '__main__':
    unittest.main()    