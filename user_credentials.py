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

        Usercredentials.user_credential_list.append(self)