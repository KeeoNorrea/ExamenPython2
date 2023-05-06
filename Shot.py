class Shots:

    def __init__(self):
        self.__nombre = None
        self.__precio = None
        self.__grados = None

    @property
    def nombre(self):
        return self.__nombre 
    @property
    def precio(self):
        return self.__precio
    @property
    def grados(self):
        return self.__grados
    
    @nombre.setter
    def nombre(self,data):
        self.__nombre = data

    @precio.setter
    def precio(self,data):
        self.__precio = data

    @grados.setter
    def grados(self,data):
        self.__grados = data



