
import veicolo 

class Auto(veicolo.Veicolo):
    def __init__(self, targa : str):
        super().__init__(targa)
        self.__maxPasseggeri = 0
        self.__passeggeri = 0
        self.__merce = 0
        self.__maxMerce = 0
    
    @property
    def maxPasseggeri(self):
        return self.__maxPasseggeri
    
    @maxPasseggeri.setter
    def maxPasseggeri(self,value: int ):
        if value < 1 and value > 9:
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
        if value < 0 and value > 1500:
            raise ValueError("Troppi o pochi chili")
        self.__maxMerce = value
        return
    
    @property
    def merce(self):
        return self.__passeggeri
    
    @merce.setter
    def merce(self,value):
        if value < 0 and value > self.__MaxMerce:
            raise ValueError("non puo trasportare così tanta merce")
        self.__merce = value
        
    def __str__(self):
        return "Auto: " + str(self.__dict__)



if __name__ == "__main__":
    auto = Auto("HA 324 ZR")
    auto.marca = "BMW"
    auto.modello = "coupè"
    auto.colore = "nero"
    auto.cilindrata = 4395
    auto.alimentazione = "benzina"
    auto.maxPasseggeri = 5
    auto.passeggeri = 2
    auto.maxMerce = 600
    auto.merce = 120
    print(auto)