class Developer:
    def __init__(self, id_developera: int, imie: str, nazwisko: str):
        self.id_developera = id_developera
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return f'Developer o ID {self.id_developera}:\n, Imie: {self.imie}\n Nazwisko: {self.nazwisko}\n'
