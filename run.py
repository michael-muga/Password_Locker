#!/usr/bin/env/python3.8
from os import uname
from user import User
from user_credentials import Usercredentials

def create_user(fname,lname,email,uname,password):
    '''
    function to create a new user
    '''
    new_user = User(fname,lname,email,uname,password)
    return new_user

def create_user_credentials(siteName,password):
    '''
    function to create a new user credential
    '''
    for user in User:
        new_credentials = Usercredentials(siteName,password)
        return new_credentials

def save_user(user):
    '''
    function to save user to the userlist using the save user method
    '''

    user.save_user()

def save_user_credentials(user_credentials):

    '''
    function for saving users credentials
    '''

    user_credentials.save_credentials()

def delete_credentials(user_credentials):
    '''
    function for deleting a whole user credential
    '''

    user_credentials.delete_credential()

def user_login(uname,password):
    '''
    function to access into a users account
    '''

    return User.user_login(uname,password)

def display_credentials():
    '''
    function to display the credentials that a user has
    '''
    return Usercredentials.display_credentials()

def main():
    '''
    the main function that calls the functions that implement the behaviours
    '''
    print("Welcome to Password Locker")

    user_name = input(" please enter your user name: ")
    password = input("please enter your password: ")

if __name__ == '__main__':
    main()
    