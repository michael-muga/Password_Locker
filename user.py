class User:
    '''
    class to generate new instances of users
    '''
    user_list = [] #empty list to append users

    def __init__(self,first_name,last_name,email,user_name,password):
        '''
        method to define the properties of the object
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.user_name = user_name
        self.password = password

    def save_user(self):
        '''
        method to save a user in to the user list
        '''

        User.user_list.append(self)