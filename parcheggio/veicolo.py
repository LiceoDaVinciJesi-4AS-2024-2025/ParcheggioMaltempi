
listaMarche = ["fiat", "alfa Romeo", "ferrari", "audi","bmw","volkswagen","porsche","ktm","ducati","yamaha","kawasaki"]
listaColori = ["rosso", "blue", "giallo", "bianco", "nero", "grigio", "verde","arancione"]
listaAlimentazioni = ["benzina", "diesel", "elettrico", "ibrido benzina", "ibrido diesel", "miscela",]

class Veicolo:
    def __init__(self, targa:str):

        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numeri = "0123456789"
        
        if len(targa) != 9:
            raise ValueError("Targa non valida")
        
        if targa[0] not in alfabeto or targa[1] not in alfabeto or targa[7] not in alfabeto or targa[8] not in alfabeto:
            raise ValueError("Targa non valida")
        
        if targa[2] != " " or targa[6] != " ":
            raise ValueError("Targa non valida")
        
        if targa[3] not in numeri or targa[4] not in numeri or targa[5] not in numeri:
            raise ValueError("Targa non valida")

        self.__targa = targa
        self.__marca = ""
        self.__modello = ""
        self.__colore = ""
        self.__cilindrata = ""
        self.__alimentazione = ""
        
      
    
    @property
    def targa(self):
        return self.__targa


    @property
    def marca(self):
        return marca
    
    @marca.setter
    def marca(self, value: str):
        if value.lower() not in listaMarche:
            raise ValueError("Marca non accettabile")
        self.__marca = value.lower()
        return
        
    @property
    def modello(self):
        return self.__modello
    
    @modello.setter
    def modello(self, value:str):
        self.__modello = value.lower()
        return
        
    
    @property
    def colore(self):
        return self.__colore
    
    @colore.setter
    def colore(self, value:str):
        if value.lower() not in listaColori:
            raise ValueError("Colore non accettabile")
        
        self.__colore = value.lower()
        return
        
    @property
    def cilindrata(self):
        return self.__cilindrata
    
    @cilindrata.setter
    def cilindrata(self, value:int):
        if value < 1000 :
            raise ValueError("Valore di cilinrata non accettabile")
        self.__cilindrata = value
        return
   
    @property
    def alimentazione(self):
        return self.__alimentazione
    
    @alimentazione.setter
    def alimentazione(self, value:str):
        if value.lower() not in listaAlimentazioni:
            raise ValueError("Alimentazione non accettabile")
        self.__alimentazione = value.lower()
        return
        

    def __str__(self):
        return "Veicolo: " + str(self.__dict__)
    
    def __repr__(self):
        return "Veicolo: " + str(self.__dict__)
    
if __name__ == "__main__":
    auto1 = Veicolo("EB 000 LA")
    auto1.marca = "ferrari"
    auto1.modello = "La Ferrari"
    auto1.colore = "nero"
    auto1.cilindrata = 6262
    auto1.alimentazione = "benzina"
    print(auto1)