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

    def test_save_credential(self):

        self.new_credentials.save_credentials()
        self.assertEqual(len(Usercredentials.user_credential_list),1)

if __name__ == '__main__':
    unittest.main()    