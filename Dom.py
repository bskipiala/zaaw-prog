from Obiekt import Obiekt


class Dom(Obiekt):
    def __init__(self, adres: int, powierzchnia: int, cena: float):
        super().__init__(self, adres, powierzchnia, cena)
        self.typ_obiektu = "Dom"

    def __str__(self):
        return f'{self.typ_obiektu} o adresie {self.adres} ma powierzchnię {self.powierzchnia} i cenę {self.cena}'
