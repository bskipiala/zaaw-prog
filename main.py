from Developer import Developer
from Zamowienie import Zamowienie
from Dom import Dom
from Mieszkanie import Mieszkanie

dom1 = Dom("ul. Słoneczna 12", 140, 800000)
mieszkanie1 = Mieszkanie("ul. Słoneczna 12", 70, 400000, 7)
developer1 = Developer(22, "Jan", "Kowalski")
lista_obiektow = [dom1, mieszkanie1]
z1 = Zamowienie(1, developer1, lista_obiektow)

wartosc_z1 = z1.policz_wartosc()
powierzchnia_z1 = z1.policz_powierzchnie()

print(wartosc_z1)
print(powierzchnia_z1)
