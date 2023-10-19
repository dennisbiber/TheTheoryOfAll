from sympy import E, I, pi, simplify

plusX = -E**(I*pi)*I**(4)**(0.5)
negX =  E**(I*pi)*I**(4)**(0.5)
plusY = pi**(0.5)
negY = -pi**(0.5)
plusZ = (I*pi)**(0.5)
negZ = (-I*pi)**(0.5)
plusW = (pi**2 + I*pi**2) **(0.5)
negW = -(pi**2 + I*pi**2) **(0.5)
zero = 0
realValues = [
    plusX,
    negX,
    plusY,
    negY,
    plusZ,
    negZ,
    plusW,
    negW,
    zero
]

def Entanglement(a, b, c):
    return (c**(2) + (a**(2) + b**(2))**(2))**(1/2)

def thing(x):
  return Entanglement(x[8], x[7], Entanglement(x[6], x[5], Entanglement(x[4], x[3], Entanglement(x[2], x[1], x[0]))))
# def thing2(x):
#   return u.Entanglement(x[6], x[5], u.Entanglement(x[4], x[3], u.Entanglement(x[2], x[1], x[0])))
answer = thing(realValues)
squareRoot2 = 2**(1/2) # 1.4142135623731

def BiberConjecture(x, y):
  return (x**(answer) + (y**(answer))**(2))

from cmath import tan, atan
# when exponent is 0, number is ~1.55740...
# when exponent is 2, number is 2.708^(302)
# when exponent is 3, number is i
# when exponent is 4, number is i
# when exponent is 6, number is -1
# when exponent is 12, number is 1
x = simplify(tan(answer**0))
y = simplify(tan(answer**2))
z = simplify(tan(answer**3))
w = simplify(tan(answer**4))
print(x)
print(y)
print(z)
print(w)
if w == z:
   print("True")
