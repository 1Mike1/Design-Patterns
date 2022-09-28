import imp
from android import Android
from ios import IOS

class Factory(object):

    @staticmethod
    def create_instance(value):
        if value.lower()=="android":
            return Android()
        elif value.lower()=="ios":
            return IOS()
        else:
            return None
        