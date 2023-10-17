from sympy import I, pi


class TheMathFunction:
    def __init__(self):
        A = I*pi # space
        m = 0 # spacetime
        p = pi # time 
        c = I**4 /(I**4 - ((-pi**2 + pi**2)/2)**2/(pi**2))**(1/2) #joules/-volume 
        """
        l = 1 / sqrt(1 - v^2/c^2) lorentz factor
        1 = l when v^2/c^2 = ((x - y)**(4))/2 when x = I*pi**2 and y = pi**2
        """
        self.Everything = ((((A**(c/I) + (m**I + p**I)**(c/I)))**(0)))**2 + (c/((((A**(c/I) + (m**I + p**I)**(c/I)))**(0))))**2
        # self.Everything = mass*(speed of light)^2

    def divisionFactors(self):
        e = self.Everything
        """
        8 = realFactor**(2) + complexFactor**(2)
        0.5 = realFactor**(2) - complexFactor**(2)
        cos(pi/4)**(2) = realFactor**(2) + complexFactor**(2)
        """
        realFactor = (e**2 + (1/e)**2) ** (1/2)
        print(realFactor)
        complexFactor = (e**2 + (I/e)**2) ** (1/2)
        return [realFactor, complexFactor]

    def inversDivisionFactors(self):
        e = self.Everything
        """
        8 = realFactor**(2) + complexFactor**(2)
        -0.5 = realFactor**(2) - complexFactor**(2)
        """
        realFactor = (e**2 - (1/e)**2) ** (1/2)
        complexFactor = (e**2 - (I/e)**2) ** (1/2)
        return [realFactor, complexFactor]
    
    def RealDivisions(self):
        N = self.divisionFactors()
        IofN = self.inversDivisionFactors()
        return [N, IofN]

    def CdivisionFactors(self):
        e = self.Everything
        """
        0 = realFactor**(2) + complexFactor**(2)
        2 = realFactor**(2) - complexFactor**(2)
        cos(pi/4)**(2) = realFactor**(2) + complexFactor**(2)
        """
        realFactor = (e**2 * (1/e)**2) ** (1/2)
        complexFactor = (e**2 * (I/e)**2) ** (1/2)
        return [realFactor, complexFactor]

    def CinversDivisionFactors(self):
        e = self.Everything
        """
        0 = realFactor**(2) + complexFactor**(2)
        32 = realFactor**(2) - complexFactor**(2)
        """
        realFactor = (e**2 / (1/e)**2) ** (1/2)
        complexFactor = (e**2 / (I/e)**2) ** (1/2)
        return [realFactor, complexFactor]
    
    def ComplexDivisions(self):
        N = self.CdivisionFactors()
        IofN = self.CinversDivisionFactors()
        return [N, IofN]

    def mulitplyFactors(self):
        e = self.Everything
        """
        8 = realFactor**(2) + complexFactor**(2)
        8 = realFactor**(2) - complexFactor**(2)
        """
        realFactor = (e**2 + (1*e)**2) ** (1/2)
        complexFactor = (e**2 + (I*e)**2) ** (1/2)
        return [realFactor, complexFactor]

    def inverseMulitplyFactors(self):
        e = self.Everything
        """
        8 = realFactor**(2) + complexFactor**(2)
        -8 = realFactor**(2) - complexFactor**(2)
        """
        realFactor = (e**2 - (1*e)**2) ** (1/2)
        complexFactor = (e**2 - (I*e)**2) ** (1/2)
        return [realFactor, complexFactor]
    
    def RealMultiplications(self):
        N = self.mulitplyFactors()
        IofN = self.inverseMulitplyFactors()
        return [N, IofN]

    def CmulitplyFactors(self):
        e = self.Everything
        """
        0 = realFactor**(2) + complexFactor**(2)
        32 = realFactor**(2) - complexFactor**(2)
        """
        realFactor = (e**2 * (1*e)**2) ** (1/2)
        complexFactor = (e**2 * (I*e)**2) ** (1/2)
        return [realFactor, complexFactor]

    def CinverseMulitplyFactors(self):
        e = self.Everything
        """
        0 = realFactor**(2) + complexFactor**(2)
        2 = realFactor**(2) - complexFactor**(2)
        """
        realFactor = (e**2 / (1*e)**2) ** (1/2)
        complexFactor = (e**2 / (I*e)**2) ** (1/2)
        return [realFactor, complexFactor]
    
    def ComplexMultiplications(self):
        N = self.CmulitplyFactors()
        IofN = self.CinverseMulitplyFactors()
        return [N, IofN]

    def eulerFactors(self):
        e = self.Everything
        """
        8.0 + (4 + 4*I)**1.0 = realFactor**(2) + complexFactor**(2)
        8.0 - (4 + 4*I)**1.0 = realFactor**(2) - complexFactor**(2)
        """
        realFactor = (e**2 + e**2) ** (1/2)
        complexFactor = (e**2 + I*e**2) ** (1/2)
        return [realFactor, complexFactor]

    def inverseEulerFactors(self):
        e = self.Everything
        """
        (4 - 4*I)**1.0 = realFactor**(2) + complexFactor**(2)
        -(4 - 4*I)**1.0 = realFactor**(2) - complexFactor**(2)
        0^4 = (realFactor**(2) - complexFactor**(2))
        """
        realFactor = (e**2 - e**2) ** (1/2)
        complexFactor = (e**2 - I*e**2) ** (1/2)
        return [realFactor, complexFactor]
    
    def RealComplexes(self):
        N = self.eulerFactors()
        IofN = self.inverseEulerFactors()
        return [N, IofN]

    def CeulerFactors(self):
        e = self.Everything
        """
        16*(1.0 + I**1.0) = realFactor**(2) + complexFactor**(2)
        16*(1.0 - I**1.0) = realFactor**(2) - complexFactor**(2)
        """
        realFactor = (e**2 * e**2) ** (1/2)
        complexFactor = (e**2 * I*e**2) ** (1/2)
        return [realFactor, complexFactor]

    def CinverseEulerFactors(self):
        e = self.Everything
        """
        1 + 16.0*(-I)**1.0 = realFactor**(2) + complexFactor**(2)
        1 - 16.0*(-I)**1.0 = realFactor**(2) - complexFactor**(2)
        """
        realFactor = (e**2 / e**2) ** (1/2)
        complexFactor = (e**2 / I*e**2) ** (1/2)
        return [realFactor, complexFactor]
    
    def ComplexComplexes(self):
        N = self.CeulerFactors()
        IofN = self.CinverseEulerFactors()
        return [N, IofN]
    
    def returnAll(self):
        return [self.RealDivisions(), self.ComplexDivisions(),
                self.RealMultiplications(), self.ComplexMultiplications(),
                self.RealComplexes(), self.ComplexComplexes()]
    

def firstOrder(x, y):
    def add():
        return x**(2) + y**(2)
    def sub():
        return x**(2) - y**(2)
    return [add(), sub()]

def secondOrder(x, y):
    def multiply():
        return x**(2) * y**(2)
    def divide():
        return x**(2) / y**(2)
    return [mulitiply(), divide()]

# def thridOrder(x, y):
#     return x


everything = TheMathFunction()
All = everything.returnAll()
print(firstOrder(All[0][0][0], All[0][0][1]))
print(firstOrder(All[0][1][0], All[0][1][1]))
print(firstOrder(All[1][0][0], All[1][0][1]))
print(firstOrder(All[1][1][0], All[1][1][1]))
print(firstOrder(All[2][0][0], All[2][0][1]))
print(firstOrder(All[2][1][0], All[2][1][1]))
print(firstOrder(All[3][0][0], All[3][0][1]))
print(firstOrder(All[3][1][0], All[3][1][1]))
print(firstOrder(All[4][0][0], All[4][0][1]))
print(firstOrder(All[4][1][0], All[4][1][1]))
print(firstOrder(All[5][0][0], All[5][0][1]))
print(firstOrder(All[5][1][0], All[5][1][1]))


