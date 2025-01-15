class Moto(Veicolo):
    def __init__(self, targa : str):
        self.__maxPasseggeri = 0
        self.__passeggeri = 0
        self.__merce = 0
        self.__maxMerce = 0
        
    @property
    def maxPasseggeri(self):
        return self.__maxPasseggeri
    
    @maxPasseggeri.setter
    def maxPasseggeri(self,value: int ):
        if value < 1 and value > 2:
            raise ValueError("Troppi posti")
        self.__maxPasseggeri = value
        return
    
    @property
    def passeggeri(self):
        return self.__passeggeri
    
    @passeggeri.setter
    def passeggeri(self,value):
        if value < 0 and value > self.__MaxPasseggeri:
            raise ValueError("Numero di passeggeri impossibile")
        self.__passeggeri = value
        
    @property
    def maxMerce(self):
        return self.__maxMerce
    
    @maxMerce.setter
    def maxMerce(self,value: int ):
        if value < 0 and value > 50:
            raise ValueError("Troppi tanti o pochi chili")
        self.__maxMerce = value
        return
    
    @property
    def merce(self):
        return self.__passeggeri
    
    @merce.setter
    def merce(self,value):
        if value < 0 and value > self.__MaxMerce:
            raise ValueError("Numero di kg di merce impossibile")
        self.__merce = value
    def __str__(self):
        return "Moto: " + str(self.__dict__)
