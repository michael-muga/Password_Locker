class Usercredentials:
    '''
    class to generate new instances of usercredentials
    '''

    user_credential_list = [] #empty list for user creddential

    def __init__(self,site_name,password):
        '''
        method to define properties of the object
        '''

        self.site_name = site_name
        self.password = password

    def save_credentials(self):

        '''
        method to save a credential into the user credential list
        '''

        Usercredentials.user_credential_list.append(self)

    def delete_credentials(self):
        '''
        method to delete saved credential
        '''
        Usercredentials.user_credential_list.remove(self)

    @classmethod
    def display_credentials(cls):
        return cls.user_credential_list