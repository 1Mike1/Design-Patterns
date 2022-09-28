from abc import ABCMeta, abstractstaticmethod

class OS(metaclass=ABCMeta):

    @abstractstaticmethod
    def specs():
        """ Interface for OS class """
    