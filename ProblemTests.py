import unittest
from Problem import Osoba, Sort

class ProblemTest(unittest.TestCase):

    def test_typ_imie_true(self):
        os = Osoba("Jan", "Nazwisko", 48)
        self.assertIs(str, type(os.get_imie()))

    def test_typ_imie_false(self):
        os = Osoba(3, "Nazwisko", 48)
        self.assertIsNot(str, type(os.get_imie()))

    def test_typ_nazw_true(self):
        os = Osoba("Imie", "Nazwisko", 76)
        self.assertIs(str, type(os.get_nazw()))

    def test_typ_wiek(self):
        os = Osoba("mam", "Nazwisko", 20)
        self.assertIs(int, type(os.get_wiek()))

    def test_zakres_ujemny_wiek(self):
        os = Osoba("m","n",10)

        self.assertTrue(os.wiek > 0)

    def test_wiek_urodziny(self):
        os = Osoba("m", "n", 10)

        self.assertTrue(os.urodziny() == 11)

    def test_imie_isupper(self):
        os = Osoba("Imie",'Nazwisko',34)

        self.assertTrue(os.imie[0].isupper())

    def test_nazw_isupper(self):
        os = Osoba("Imie", 'Nazwisko', 34)

        self.assertTrue(os.nazwisko[0].isupper())


    def test_dodaj_true(self):
        el = [Osoba("Jan", "Nazwisko1", 20),
              Osoba("Ola", "Nazwisko2", 14)]
        jan = Osoba("Jan", "Nazwisko1", 20)

        self.assertEqual("Dodano", Sort(el).dodaj(jan))

    def test_dodaj_false(self):
        el = [Osoba("Jan", "Nazwisko1", 20),
              Osoba("Ola", "Nazwisko2", 14)]
        jan = Osoba(4, "Nazwisko1", 20)

        self.assertEqual("Złe dane",Sort(el).dodaj(jan))

    def test_sort_wiek(self):
        el = [Osoba("Jan", "Nazwisko1", 20),
              Osoba("Ola", "Nazwisko2", 14),
              Osoba("Kuba", "Nazwisko3", 23)]

        self.listaA = [el[1],el[0],el[2]]
        self.listaB = Sort(el).sort_wiek()

        self.assertListEqual(self.listaA, self.listaB)

    def test_sort_imie_true(self):
        el = [Osoba("Jan", "Nazwisko1", 20),
              Osoba("Ola", "Nazwisko2", 14),
              Osoba("Kuba", "Nazwisko3", 23)]

        self.listaA = [el[0], el[2], el[1]]
        self.listaB = Sort(el).sort_imie()

        self.assertListEqual(self.listaA, self.listaB)

    def test_sort_imie_false(self):
        el = [Osoba("Jan", "Nazwisko1", 20),
              Osoba(5, "Nazwisko2", 14),
              Osoba("Kuba", "Nazwisko3", 23)]

        os = Sort(el)

        self.assertEqual("-- Imie nie moze byc liczba --", os.sort_imie())


if __name__ == '__main__':
    unittest.main()
