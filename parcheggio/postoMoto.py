
import moto
import datetime

class PostoMoto:
    def __init__(self, numeroPosto:str):
        
        self.__numeroPosto = numeroPosto
        self.__tipoParceggio = "Moto"
        self.__occupato = False
        self.__motoParcheggiata= "/"
        self.__dataTermine = "/"
        
    @property
    def numeroPosto(self):
        return self.__numeroPosto
    
    @property
    def tipoParcheggio(self):
        return self.__tipoParceggio
    
    @property
    def occupato(self):
        return self.__occupato
    
    @property
    def motoParcheggiata(self):
        return self.__motoParcheggiata
    
    @property
    def dataTermine(self):
        return self.__dataTermine
    
    def occupaPosto(self, veicolo:moto.Moto, dataTermine:datetime.date):
        if self.__occupato == True:
            raise ValueError(f"Il posto {self.__numeroPosto} è già occupato dalla moto {self.__motoParcheggiata}")
        
        adesso = datetime.datetime.now()
        if dataTermine < adesso:
            raise ValueError("Non puoi inserire una data passata")
        
        self.__occupato = True
        self.__motoParcheggiata = veicolo
        self.__dataTermine = dataTermine
        
        return True
    
    def liberaPosto(self):
        if self.__occupato == False:
            raise ValueError(f"Il posto {self.__numeroPosto} è già libero!")
        
        self.__occupato = False
        self.__motoParcheggiata = "/"
        self.__dataTermine = "/"
        
        return True
    
    
    def __str__(self):
        return "Posto: " + str(self.__dict__)
    
    def __repr__(self):
        return "Posto: " + str(self.__dict__)
        
    

if __name__ == "__main__":
    moto1 = moto.Moto("VL 254 LU")
    moto1.marca = "kawasaki"
    moto1.modello = "ninja H2R"
    moto1.alimentazione = "diesel"
    moto.colore = "Rosso"
    moto1.maxPasseggeri = 2
    moto1.passeggeri = 2
    print(moto1)
    print("----------------------------------------------------------------------------------------------------------------------------------")
    parcheggio1 = PostoMoto("0")
    print(parcheggio1)
    print("----------------------------------------------------------------------------------------------------------------------------------")
    parcheggio1.occupaPosto(moto1, datetime.datetime(2025, 5, 2, 0, 0, 0))
    print(parcheggio1)
    print("----------------------------------------------------------------------------------------------------------------------------------")
    parcheggio1.liberaPosto()
    print(parcheggio1)