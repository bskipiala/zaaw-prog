from Obiekt import Obiekt


class Mieszkanie(Obiekt):
    def __init__(self, adres: int, powierzchnia: int, cena: float, pietro: int):
        super().__init__(self, adres, powierzchnia, cena)
        self.typ_obiektu = "Mieszkanie"
        self.pietro = pietro

    def __str__(self):
        return f'{self.typ_obiektu} o adresie {self.adres}' \
               f' ma powierzchnię {self.powierzchnia} i cenę {self.cena}' \
               f' oraz znajduje się na {self.pietro} piętrze'
