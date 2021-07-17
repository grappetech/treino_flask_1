import string

from erp.models.entity import Entity


class User(Entity):
    def __init__(self):
        return

    __username__: string
    __name__: string
    __password__: string
    __email__: string
    __phone__: string
    __active__: bool

    def get_username(self):
        return self.__username__

    def set_username(self, username: string):
        self.__username__ = username

    def get_name(self):
        return self.__name__

    def set_name(self, name: string):
        self.__name__ = name

    def get_password(self):
        return self.__password__

    def set_password(self, password: string):
        self.__password__ = password

    def get_email(self):
        return self.__email__

    def set_email(self, email: string):
        self.__email__ = email

    def get_phone(self):
        return self.__phone__

    def set_phone(self, phone: string):
        self.__phone__ = phone

    def get_active(self):
        return self.__active__

    def set_active(self, active: bool):
        self.__active__ = active

