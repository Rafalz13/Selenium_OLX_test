import unittest
from Problem import Osoba

class ProblemTest(unittest.TestCase):

    def test_typ_imie(self):
        os =  Osoba("Jan", "Nazwisko", 48)
        self.assertIs(str, type(os.get_imie()))

    def type_typ_nazw(self):
        os = Osoba("Imie", "Nazwisko", 76)
        self.assertIs(str, type(os.get_nazw()))

    def test_typ_wiek(self):
        os = Osoba("mam", "Nazwisko", 20)
        self.assertIs(int, type(os.get_wiek()))

    def test_zakres_ujemny_wiek(self):
        os = Osoba("m","n",-10)
        self.assertTrue(os.wiek > 0)

    def test_wiek(self):
        os = Osoba("m", "n", 10)
        self.assertTrue(os.urodziny() == 11)

    def test_imie_isupper(self):
        os = Osoba("Imie",'Nazwisko',34)
        self.assertTrue(os.imie[0].isupper())

    def test_nazw_isupper(self):
        os = Osoba("Imie", 'Nazwisko', 34)
        self.assertTrue(os.nazwisko[0].isupper())

    def test_sort_wiek(self):
        pass

    def test_sort_imie(self):
        pass