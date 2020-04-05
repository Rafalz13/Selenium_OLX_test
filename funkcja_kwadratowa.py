from math import sqrt

class Fun_kwadr(object) :
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.x1 = None
        self.x2 = None
        self.delta

    def delta(self):
        self.delta = (self.b * self.b) - 4 * self.a * self.c
        print(f'delta = {self.delta}')

        
    def miejsca_zerowe(self):
        if self.delta > 0:
            self.x1 = (-1 * self.b - sqrt(self.delta) ) / (2 * self.a)
            self.x2 = (-1 * self.b + sqrt(self.delta) ) / (2 * self.a)
            print(f'x1 : {self.x1}\nx2 : {self.x2}' )
        elif self.delta == 0:
            self.x1 = -1 *self.b/(2 * self.a)
            print(f'x = {self.x1}')
        elif self.delta < 0:
            print ("Funkcja nie posiada miejsc zerowych")


if __name__ =='__main__':

    funk1 = Fun_kwadr(-3,2,2)
    funk1.delta()
    funk1.miejsca_zerowe()




