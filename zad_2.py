class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self. open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Informacje o bibliotece:\nAdres: ul.{self.street}, {self.zip_code} {self.city}\nGodziny otwarcia: {self.open_hours}\nTelefon: {self.phone}'

class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str, birth_date: str, city: str, street: str, zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Informacje o pracowniku:\nImię: {self.first_name}\nNazwisko: {self.last_name}\nData zatrudnienia: {self.hire_date}\nData urodzenia: {self.birth_date}\n\nAdres: ul.{self.street}, {self.zip_code} {self.city}\nTelefon: {self.phone}'

class Order:
    def __init__(self, employee: Employee, student: str, books: list, order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Informacje o zamówieniu:\nStudent zamawiający: {self.student}\nZamawiane książki: {self.books}\nPracownik: {self.employee}\nData zamówienia: {self.order_date}'


class Book:
    def __init__(self, library: Library, publication_date: str, author_name: str, author_surname: str, number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Informacje o książce:\nBiblioteka: {self.library}\nData publikacji: {self.publication_date}\nAutor: {self.author_name} {self.author_surname}\nLiczba stron: {self.number_of_pages}'

