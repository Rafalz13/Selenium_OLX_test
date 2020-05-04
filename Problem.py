class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek


    def urodziny(self):
        self.wiek += 1
        return self.wiek

    def get_imie(self):
        return self.imie

    def get_wiek(self):
        return self.wiek

    def get_nazw(self):
        return self.nazwisko


class Sort:

    def __init__(self,lista):
        self.lista = lista

    def dodaj(self,dodaj):
        if type(dodaj.imie) is str and type(dodaj.nazwisko) is str and type(dodaj.wiek) is int:
            self.lista.append(dodaj)
            return "Dodano"
        else:
            return "Złe dane"


    def sort_imie(self):
        try:
            self.lista.sort(key=lambda x: x.imie)
            return self.lista
        except TypeError:
            return "-- Imie nie moze byc liczba --"

    def sort_wiek(self):
        self.lista.sort(key=lambda x: x.wiek)
        return self.lista

    def wypisz(self):
        for obj in self.lista:
            print(str(obj.imie) + " " + str(obj.nazwisko) + " " + str(obj.wiek))




def main():

    elements = [Osoba("Jan", "Nazwisko1", 20),
                Osoba("Ola", "Nazwisko2", 40),
                Osoba("Kuba", "Nazwisko3", 23),
                Osoba("Eli", "Nazwisko4", 30)]

    Franek = Osoba("Kat","Mag",33)

    lista1 = Sort(elements)
    lista1.dodaj(Franek)


if __name__ == "__main__":
    main()