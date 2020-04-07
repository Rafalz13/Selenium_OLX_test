
from math import sqrt


class Kwadratowa:
    """

    >>> Kwadratowa(2,4,6).delta()
    -32.0

    >>> Kwadratowa(20,40,60).delta()
    -3200.0

    >>> Kwadratowa(2,6,-8).delta()
    100.0


    >>> Kwadratowa(5,4,2).miejsca_zerowe()
    Brak miejsc

    >>> Kwadratowa(1,2,1).miejsca_zerowe()
    x = -1.0

    >>> Kwadratowa(2,6,-8).miejsca_zerowe()
    x1 = -4.0
    x2 = 1.0


    >>> Kwadratowa("5",6,"1.0").miejsca_zerowe()
    x1 = -1.0
    x2 = -0.2

    >>> Kwadratowa(0,6,-2).miejsca_zerowe()
    Traceback (most recent call last):
    ZeroDivisionError: float division by zero

    """

    def __init__(self,a,b,c):
        try:
            self.a = float(a)
            self.b = float(b)
            self.c = float(c)
            self.x1 = None
            self.x2 = None

        except ValueError:
            print("Klasa przyjmuje liczby")
        except AttributeError:
            print("BLAD")


    def delta(self):
        return float((self.b * self.b) - 4 * self.a * self.c)



    def miejsca_zerowe(self):
        try:
            1/self.a
        except ZeroDivisionError as e:
            print(e)

        if self.delta() > 0:
            self.x1 = (-1 * self.b - sqrt(self.delta()) ) / (2 * self.a)
            self.x2 = (-1 * self.b + sqrt(self.delta()) ) / (2 * self.a)
            print(f'x1 = {self.x1}\nx2 = {self.x2}' )
        elif self.delta() == 0:
            self.x1 = -1 *self.b/(2 * self.a)
            print(f'x = {self.x1}')
        elif self.delta() < 0:
            print("Brak miejsc")


if __name__ =='__main__':
    import doctest
    doctest.testmod()
    # funk1 = Kwadratowa(2,5,-1)
    # funk1.delta()
    # funk1.miejsca_zerowe()




