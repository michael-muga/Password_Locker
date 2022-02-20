import unittest

from user import User

class TestUser(unittest.TestCase):
    '''
    test class that defines test cases for the User class behaviors
    '''

    def setUp(self):

        self.new_user = User("michael","muga","michael@gmail.com","mike","febr2000")

    def test__init(self):
        '''
        test case to test if the obect is initialised properly
        '''

        self.assertEqual(self.new_user.first_name,"michael")
        self.assertEqual(self.new_user.last_name,"muga")
        self.assertEqual(self.new_user.email,"michael@gmail.com")
        self.assertEqual(self.new_user.user_name,"mike")
        self.assertEqual(self.new_user.password,"febr2000")


    def test_save_user(self):
        '''
        test case to test if the user is saved into the the user list
        '''

        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
    unittest.main()