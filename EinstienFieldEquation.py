from sympy import E, I, pi, cos, tan, sin
import cmath
# o/pi^2 + i*pi^2 (complex zero) or infinitiy. What ever helps you picture it. (Imagination)
# -1/1 = Magntiude (complex space)
# pi = positive energy
# I*pi = negative energy
# -e^(I*pi)/e^(I*pi) = Units (complex Time) 

# # Define the stress-energy-momentum tensor
#      [I*pi, 0, E**(I*pi), pi, o, o],
#      [o, pi, 0, E**(I*pi), pi, o],
#      [o, o, pi, E**(I*pi), 0, pi],
#      [pi, o, o, pi, 0, E**(I*pi)],
#      [E**(I*pi), pi, o, o, E**(I*pi), 0],
#      [0, E**(I*pi), pi, o, o, pi]

# v = pi**2 + I*pi**2  # 1st order, 1st dimension velocity -> (Complex 0) (vacuum)
# y = -I*pi # 2nd order, 1st dimension magnitude + (Tensor Level) ((Lower Limit Time)) (negative energy)
# x = -pi # 1st order, 2nd dimension Time +- (negative natural unit) (Lower Limit Space) (positive energy)
# z = 1 # 2nd order, 2nd dimension magntiude + o - (Matrix Level) (median of Complex 0 and all 4 natural units) ()
# t = pi # 2nd order, 3rd dimension Space -volume/+volume (Upper Limit Space)
# c = E**(I*pi) # 2nd order, Complex dimension volume maximum (vector Level) (Upper Limit Time)
# m = 1 # 2nd order, mass joules/volume/second (solution = (joules**(-volume)). volume = 1/kg (Real 1)

class SpaceTensor:
    def __init__(self, timeDireciton = 1):
        v = pi**2 + I*pi**2 
        y = timeDireciton * -I*pi 
        x = timeDireciton* -pi 
        z = timeDireciton* 1 
        t = timeDireciton* pi 
        c = timeDireciton * E**(I*pi) 
        m = timeDireciton * 1 
        row1 = [m, c, t, z, x, y, v]
        row2 = [v, m, c, t, z, x, y]
        row3 = [y, v, m, c, t, z, x]
        row4 = [x, y, v, m, c, t, z]
        row5 = [z, x, y, v, m, c, t]
        self.row6 = [t, z, x, y, v, m, c] # infinity (should be able to be meausred via entanglement)
        self.row7 = [c, t, z, x, y, v, m]
        self.rows = [row1,row2,row3,row4,row5]
        self._matricesTensor = []
        self._negativeI = E**(I*(cmath.cos(pi/4)+I*cmath.sin(pi/4)))

    def FieldEquation(self, x): # complex zero (Pythagorean)
        m, c, t, z, x, y, v = x[0::]
        return (v**2 + (y*I**4)**(x**3 + (z*I)**(t**2 + pi*I**(m * c**(pi**(-I)))))**2)**(1/2)
    
    def ComplexMatrix(self, x): # 
        m, c, t, z, x, y, z = x[0::]
        return (y*I**4)**(x**3 + (z*I)**(t**2 + pi*I**(m * c**(pi**(-I)))))
    
    def fetchRealMatrices(self):
        for row in self.rows:
            self._matricesTensor.append(self.FieldEquation(row))
        self._matricesTensor.append(self.ComplexMatrix(self.row6)) 
        self._matricesTensor.append(self.FieldEquation(self.row7))

    def getMaxValues(self):
        self.fetchRealMatrices()
        matrix = self._matricesTensor
        v = matrix[0]**2
        theRest = (matrix[1]**2 + matrix[2] *( matrix[3] + matrix[4]*(matrix[5] + matrix[6])))**2
        return E**(I*((cmath.tan(cos((v**2 + I*theRest**2)**(1/2)) + I*sin(theRest**2 + I*v**2)**(1/2))**(1/2))))

    def getMinimumValue(self):
        return self._negativeI


spaceTensor = SpaceTensor(timeDireciton=-1)
allThings = spaceTensor.getMaxValues()
noThings = spaceTensor.getMinimumValue()
print(allThings)
print(noThings)
if allThings == noThings:
  print("Yes")