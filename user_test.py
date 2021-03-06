import unittest

from user import User

class TestUser(unittest.TestCase):
    '''
    test class that defines test cases for the User class behaviors
    '''

    def setUp(self):
        '''
        The method that runs before each test case
        '''

        self.new_user = User("michael","muga","michael@gmail.com","mike","febr2000")

    def test__init(self):
        '''
        test case to test if the object is initialised properly
        '''

        self.assertEqual(self.new_user.first_name,"michael")
        self.assertEqual(self.new_user.last_name,"muga")
        self.assertEqual(self.new_user.email,"michael@gmail.com")
        self.assertEqual(self.new_user.user_name,"mike")
        self.assertEqual(self.new_user.password,"febr2000")

    def tearDown(self):
        '''
        method to clean up after each test case has run
        '''
        User.user_list = []


    def test_save_user(self):
        '''
        test case to test if the user is saved into the the user list
        '''

        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_users(self):
        '''
        test case for testing saving multiple users into the user list
        '''
        self.new_user.save_user()
        test_user = User("john","cena","cena2yahoo.com","jcena","67567")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)


    def test_user_login(self):
        '''
        test for user to login with the username and password
        '''

        self.new_user.save_user()
        test_user = User("john","cena","cena2yahoo.com","jcena","67567")
        test_user.save_user()

        loggedin_user = User.user_login("jcena","67567")
        self.assertEqual(loggedin_user.email,test_user.email)

if __name__ == '__main__':
    unittest.main()