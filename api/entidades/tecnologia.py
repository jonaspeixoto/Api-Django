class Tecnologia():
    def __init__(self):
        self.__nome = None

    def __int__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
