from Obiekt import Obiekt
from Developer import Developer


class Zamowienie:
    def __init__(self, numer_zamowienia: int, developer: Developer, *lista_obiektow: Obiekt):
        self.numer_zamowienia = numer_zamowienia
        self.lista_obiektow = lista_obiektow
        self.developer = developer

    def __str__(self):
        return f'Zamowienie o numerze {self.numer_zamowienia}:\n ' \
               f'Zamowione obiekty: {self.lista_obiektow}\n ' \
               f'Wartosc zamowienia: {self.wartosc_zamowienia}\n ' \
               f'Developer obsługujący zamowienie: {self.developer}'

    def setNumerZamowienia(self, nr):
        self.numer_zamowienia = nr

    def setDeveloper(self, dev):
        self.developer = dev

    def setListaObiektow(self, lo):
        self.lista_obiektow = lo

    def policz_wartosc(self):
        wartosc = 0.0
        for obiekt in self.lista_obiektow:
            wartosc = wartosc + obiekt.cena
        return wartosc

    def policz_powierzchnie(self):
        powierzchnia = 0
        for obiekt in self.lista_obiektow:
            powierzchnia = powierzchnia + obiekt.powierzchnia
        return powierzchnia
