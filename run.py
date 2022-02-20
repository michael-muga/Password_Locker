#!/usr/bin/env/python3.8
from user import User
from user_credentials import Usercredentials

def create_user(fname,lname,email,uname,password):

    new_user = User(fname,lname,email,uname,password)
    return new_user

def create_user_credentials(siteName,password):

    for user in User:
        new_credentials = Usercredentials(siteName,password)
        return new_credentials

def save_user(user):

    user.save_user()

def save_user_credentials(user_credentials):

    user_credentials.save_credentials()

def delete_credentials(user_credentials):

    user_credentials.delete_credential()

def user_login(uname,password):

    return User.user_login(uname,password)

def display_credentials():
    
    return Usercredentials.display_credentials()