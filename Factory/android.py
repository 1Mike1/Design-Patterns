from interface import OS

class Android(OS):

    def __init__(self)->None:
        self.__os = "Android"

    def specs(self):
        return f"{self.__os}  is the most powerfull os."
