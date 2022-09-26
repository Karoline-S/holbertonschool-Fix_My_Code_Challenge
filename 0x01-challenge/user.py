#!/usr/bin/python3
""" 
User class
"""

class User():
    """ Defines class User  """

    def __init__(self):
        """ Documentation - initiates a User object """
        self.email = ""

    @property
    def email(self):
        """ gets private variable email and returns it """
        return self.__email

    @email.setter
    def email(self, value):
        """ sets private variable email after checking type """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value
   
    
if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
