class MyFraction:
    def __init__(self, numerator, denominator):
        self.numerator=numerator
        self.denominator=denominator
        
        
    def __str__(self):
        return "%d/%d" %(self.numerator,self.denominator)

    def negate(self):
        return MyFraction(self.numerator*(-1),self.denominator)
    
    def inverse(self):
        return MyFraction(self.denominator, self.numerator)

    def reduction(self):
        a=self.numerator
        b=self.denominator
        if a<b:
            a, b = b, a
        while b != 0:
                a, b = b, a%b
        self.numerator = int(self.numerator/a)
        self.denominator = int(self.denominator/a)
        return self

    def __add__(self, frac):
        if isinstance(frac,int):
            frac=MyFraction(self.denominator*frac,self.denominator*frac)
        numerator = (self.numerator*frac.denominator) + (frac.numerator*self.denominator)
        denominator = self.denominator*frac.denominator
        
        
        return MyFraction(numerator, denominator).reduction()

    def __sub__(self, frac):
        if isinstance(frac,int):
            frac=MyFraction(self.denominator*frac,self.denominator*frac)
        
        return self.__add__(frac.negate())
        
    def __mul__(self, frac):
        if isinstance(frac,int):
            frac=MyFraction(self.denominator*frac,self.denominator*frac)
        numerator = self.numerator*frac.numerator
        denominator = self.denominator*frac.denominator
        
        return MyFraction(numerator, denominator).reduction()


    def __truediv__(self, frac):
        if isinstance(frac,int):
            return self.__mul__(frac)
        
        return self.__mul__(frac.inverse())


### do not edit here
if __name__ == '__main__':
    a = MyFraction(1,2)
    b = MyFraction(13,15)
    x = a + b
    print(f'x={x}, a={a}, b={b}')

    c = x - a
    d = x - 1
    y = c / d
    print(f'y={y}, c={c}, d={d}')
