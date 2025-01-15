
marca = ["volkswagen","audi","bmw","mercedes","fiat","dacia","ferrari","lamborghini","pagani"]
colori = ["nero","giallo","rosso","verde","arancione","viola","bianca","grigia","blu","marrone"]
class veicolo:
    def __init__(self,marca:str, modello:str, colore:str, cilindrata:int,alimentazione:str, targa:str):
        self.__marca = marca
        self.__modello = modello
        self.__colore = colore
        self.__cilindrata = cilindrata
        self.__alimentazione = alimentazione
        self.__targa = "GP 483 RE"
        
    def __str__(self) :
        return str(self.__dict__)
    
    def __repr__(self) :
        return str(self.__dict__)
    
    @property
    def marca ( self) :
        return self.__marca
    
    @property
    def modello ( self) :
        return self.__modello
    
    @property
    def colore( self) :
        return self.__descrizione
    
    @colore.setter
    def colore(self,col):
        if col.lower() not in colori:
            raise ValueError (col,"non è un colore")
        self.__colore = col.lower()
        return
    
    @property
    def cilindrata( self) :
        return self.__cilindrata
    
    @cilindrata.setter
    def cilindrata (self,num:int):
        if num < 1000:
            raise ValueError ("una macchina non può avere una cilindrata minore di 1000")
    
    @property
    def alimentazione ( self) :
        return self.__alimentazione
    
    @property
    def targa ( self) :
        return self.__targa


    