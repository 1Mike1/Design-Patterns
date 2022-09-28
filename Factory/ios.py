from interface import OS

class IOS(OS):

    def __init__(self)->None:
        self.__os = "IOS"

    def specs(self):
        return f"{self.__os} is the most secure os."
    