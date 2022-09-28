from datetime import datetime

class Singleton(object):
    
    _instances = {}
    def __new__(cls, *args, **kargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__new__(cls)
        return cls._instances[cls]

class logger(Singleton):

    def __init__(self, name="log", mode="a"):
        self.__name = name
        self.__mode = mode

    def __repr__(self):
        return f'Filename:{self.__name} id:{id(self)}'

    def log(self, data):
        with open(self.__name, self.__mode) as file:
            file.write(f"{datetime.utcnow()}\t| {data}\t\n")

log = logger("log","w")
log.log(f"Testing the singleton class. The id for this instance is {log.__repr__()}")
log1 = logger()
log1.log(f"Seems Like its working. The id for this instance is {log1.__repr__()}")
print(log)
print(log1)


