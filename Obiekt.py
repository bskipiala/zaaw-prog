class Obiekt:
    def __init__(self, adres: str, typ_obiektu: str, powierzchnia: int, cena: float):
        self.adres = adres
        self.typ_obiektu = typ_obiektu
        self.powierzchnia = powierzchnia
        self.cena = cena

    def __str__(self):
        return f'{self.typ_obiektu} o adresie {self.adres}' \
               f' ma powierzchnię {self.powierzchnia} i cenę {self.cena}'

    def getAdres(self):
        return self.adres

    def getTypObiektu(self):
        return self.typ_obiektu

    def getPowierzchnia(self):
        return self.powierzchnia

    def getCena(self):
        return self.cena
