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

v = pi**2 + I*pi**2  # 1st order, 1st dimension velocity -> (Complex 0) (vacuum)
y = -I*pi # 2nd order, 1st dimension magnitude + (Tensor Level) ((Lower Limit Time)) (negative energy)
x = -pi # 1st order, 2nd dimension Time +- (negative natural unit) (Lower Limit Space) (positive energy)
z = 1 # 2nd order, 2nd dimension magntiude + o - (Matrix Level) (median of Complex 0 and all 4 natural units) ()
t = pi # 2nd order, 3rd dimension Space -volume/+volume (Upper Limit Space)
c = E**(I*pi) # 2nd order, Complex dimension volume maximum (vector Level) (Upper Limit Time)
m = 1 # 2nd order, mass joules/volume/second (solution = (joules**(-volume)). volume = 1/kg (Real 1)

row1 = [m, c, t, z, x, y, v]
row2 = [v, m, c, t, z, x, y]
row3 = [y, v, m, c, t, z, x]
row4 = [x, y, v, m, c, t, z]
row5 = [z, x, y, v, m, c, t]
row6 = [t, z, x, y, v, m, c] # infinity (should be able to be meausred via entanglement)
row7 = [c, t, z, x, y, v, m]
rows = [row1,row2,row3,row4,row5]
def FieldEquation(x): # complex zero (Pythagorean)[m, c, t, z, x, y, z]
  m, c, t, z, x, y, v = x[0::]
  return (v**2 + (y*I**4)**(x**3 + (z*I)**(t**2 + pi*I**(m * c**(pi**(-I)))))**2)**(1/2)
sums = []
for row in rows:
  sums.append(FieldEquation(row))

def Infinity(x): # 
  m, c, t, z, x, y, z = x[0::]
  return (y*I**4)**(x**3 + (z*I)**(t**2 + pi*I**(m * c**(pi**(-I)))))
sums.append(Infinity(row6))
sums.append(FieldEquation(row7))
v = sums[0]**2
theRest = (sums[1]**2 + sums[2] *( sums[3] + sums[4]*(sums[5] + sums[6])))**2

allThings = E**(I*((cmath.tan(cos((v**2 + I*theRest**2)**(1/2)) + I*sin(theRest**2 + I*v**2)**(1/2))**(1/2))))
noThings = E**(I*(cmath.cos(pi/4)+I*cmath.sin(pi/4)))
print(allThings)
print(noThings)
if allThings == noThings:
  print("Yes")