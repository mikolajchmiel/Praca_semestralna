
class DictEntry:
    def __init__(self, name, surname, date_of_birth, place_of_birth, favourite_books):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.place_of_birth = place_of_birth
        self.favourite_books = favourite_books

    def print_entry(self):
        user_data = {'Imie i nazwisko': '{} {}'.format(name, surname),
                     'Data urodzenia': date_of_birth,
                     'Miejsce urodzenia': place_of_birth,
                     'Ulubione książki': favourite_books}
        return str(user_data)

if __name__ == '__main__':
    name = str(input('jak masz na imie? \n'))
    surname = str(input('jak masz na nazwisko? \n'))
    date_of_birth = str(input('kiedy sie urodziles? \n'))
    place_of_birth = str(input('gdzie sie urodziles? \n'))
    favourite_books = []
    while True:
        book = str(input('podaj mi swoja ulubiona ksiazke! (Jeśli więcej książek nie jest godnych tego miana, wpisz <Q>) \n'))
        if book == 'Q':
            break
        else:
            favourite_books.append(book)

    new_user = DictEntry(name, surname, date_of_birth, place_of_birth, favourite_books)
    print (f'Dane postaci:{new_user.print_entry()}')