from theMathAlgorithm import Magnitudes
from sympy import E, I, pi, cos, tan, sin, Matrix


class Units:
    def __init__(self):
        self._Magnitudes = Magnitudes()
        self.two = self._Magnitudes.two()
        space = pi
        self.space = space
        self.velocity = space**self.two + I*space**self.two

    def energy(self):
        return self.Weight(1)**(self.EntanglementCoefficient * self.space)

    def SquareRoot(self):
        return self.two**self.EntanglementCoefficient()

    def LorentzFactor(self):
        # sqrt(pi**(-1)) = sqrt(1/(pi+0^2/pi^2))
        # Fundamental/Absolute
        return (pi**(self.EntanglementCoefficient()*self.two))
    
    def FieldEquationCoefficient(self):
        # 8 * pi
        # Fundamental/Absolute
        return self._Magnitudes.twoCubed() * pi
    
    def OhmsCoefficient(self):
        # Resistance = mass * energy
        # Fundamental/Absolute
        A = E**(I*pi)**(self.two**(self.EntanglementCoefficient()))
        v = pi
        return v*A
    
    # def PythagoreanCoefficient(self):
    #     # square root of 2 when energy = velocity
    #     # Fundamental/Absolute
    #     b = self.velocity
    #     a = self.energy()
    #     return self.Entanglement(b, a)
    
    def Entanglement(self, a, b):
        # pythangorean theorem
        return (a**(self.two) + b**(self.two))**self.SquareRoot()
    
    def TimeCoefficient(self):
        # s = d/t where s = velocity, d = space, t = time
        # t = d/s (pi per complex zero) meaning the current time point per previous time point
        # Fundamental/Absolute
        return self.space/self.velocity
    
    def GravityCoefficient(self):
        # FieldEquationCoefficient * AccelerationCoefficient
        # Aboslute/Emergent
        return (self.FieldEquationCoefficient() * self.AccelerationCoefficient())/self.TimeCoefficient()
    
    def AccelerationCoefficient(self):
        # a = (v-u)/t = final velocity mius initial velocity difference per time
        # a = velocity per time coefficient (pi/pi)
        # Fundamental/Absolute
        return self.velocity / self.TimeCoefficient()
    
    def EntanglementCoefficient(self):
        # -1: Using the lorentz factor when v = c and without the radical
        # Fundamental/Absolute
        return cos((self.space+(self.space**self.two/(E**(I*self.space))**(self.two))**(self.two)))
    
    def One(self):
        # -1**2
        # Fundamental/Absolute
        return self.EntanglementCoefficient()**(self.two)
    
    def DensityCoefficient(self):
        # Fundemental
        # d = m/v where m = mass and v = space when mass = 1
        return self.space**(self.EntanglementCoefficient())
    
    def Entropy(self, mass):
        # Variable/Emergent
        # F = m ×  a where m = mass and a = acceleration
        return mass * self.AccelerationCoefficient()
    
    def KineticEnergy(self, mass):
        # Variable/Emergent
        #  KE = (1/2)mv^2
        return (self.two**(self.EntanglementCoefficient())) * mass * self.velocity**(self.two)
    
    def Weight(self, mass):
        # w = m * g (cos(1.0*pi**4.0) when mass =1)
        # eulers number (e)
        g = self.Entanglement(mass, self.GravityCoefficient())
        t = self.Entanglement(self.TimeCoefficient(), self.KineticEnergy(1))
        gPerT =  self.Entanglement(g, t)
        return self.Entanglement(gPerT, self.Entropy(mass))
    

units = Units()
print(units.LorentzFactor())
print(units.FieldEquationCoefficient())
print(units.OhmsCoefficient())
# print(units.PythagoreanCoefficient())
print(units.TimeCoefficient())
print(units.AccelerationCoefficient())
print(units.EntanglementCoefficient())
print(units.One())
print(units.Weight(1)**(I*pi))
print(units.KineticEnergy(1))
