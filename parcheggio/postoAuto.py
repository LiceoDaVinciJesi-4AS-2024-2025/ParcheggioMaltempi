import auto
import datetime

class PostoAuto:
    def __init__(self, numeroPosto:str):
        
        self.__numeroPosto = numeroPosto
        self.__tipoParceggio = "Auto"
        self.__occupato = False
        self.__autoParcheggiata= " "
        self.__dataTermine = " "
        
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
    def autoParcheggiata(self):
        return self.__autoParcheggiata
    
    @property
    def dataTermine(self):
        return self.__dataTermine

    def occupaPosto(self, veicolo:auto.Auto, dataTermine:datetime.date):
        if self.__occupato == True:
            raise ValueError(f"Il posto {self.__numeroPosto} è già occupato! dalla macchina {self.__autoParcheggiata}")
                
        adesso = datetime.datetime.now()
        if dataTermine < adesso:
            raise ValueError("Non puoi inserire una data passata")
        
        self.__occupato = True
        self.__autoParcheggiata = veicolo
        self.__dataTermine = dataTermine
        
        return True
    
    def liberaPosto(self):
        if self.__occupato == False:
            raise ValueError(f"Il posto {self.__numeroPosto} è già libero!")
        
        self.__occupato = False
        self.__autoParcheggiata = " "
        self.__dataTermine = " "
        
        return True
    
    
    def __str__(self):
        return "Posto: " + str(self.__dict__)
    
    def __repr__(self):
        return "Posto: " + str(self.__dict__)
    


if __name__ == "__main__":
    macchina1 = auto.Auto("RS 666 SR")
    macchina1.marca = "audi"
    macchina1.modello = "RS6"
    macchina1.alimentazione = "benzina"
    macchina1.colore = "grigio"
    macchina1.maxPasseggeri = 5
    macchina1.passeggeri = 2
    print(macchina1)
    print("--------------------------------------------------------------------------------------------------------------------------------------")
    parcheggio1 = PostoAuto("1")
    print(parcheggio1)
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    parcheggio1.occupaPosto(macchina1, datetime.datetime(2025, 4,25, 0 , 0, 0))
    print(parcheggio1)
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    parcheggio1.liberaPosto()
    print(parcheggio1)
    