plusX = -E**(I*pi)*I**(4)**(0.5)
negX =  E**(I*pi)*I**(4)**(0.5)
plusY = pi**(0.5)
negY = -pi**(0.5)
plusZ = (I*pi)**(0.5)
negZ = (-I*pi)**(0.5)
plusW = (pi**2 + I*pi**2) **(0.5)
negW = -(pi**2 + I*pi**2) **(0.5)
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

plusLen = 1
negLen = -1
plusWidth = 1
negWidth = 1
plusDepth = 1
negDepth = -1
negTime = -1
plotList = [
    plusLen,
    negLen,
    plusWidth,
    negWidth,
    plusDepth,
    negDepth,
    negTime,

]
def pyth(x, y):
    return ((x**2 + y**2)**(0.5))

x = realValues
print(len(x))
def thing(x):
  return u.Entanglement(x[8], x[7], u.Entanglement(x[6], x[5], u.Entanglement(x[4], x[3], u.Entanglement(x[2], x[1], x[0]))))
# def thing2(x):
#   return u.Entanglement(x[6], x[5], u.Entanglement(x[4], x[3], u.Entanglement(x[2], x[1], x[0])))
answer = thing(realValues)
squareRoot2 = 2**(1/2) # 1.4142135623731
# print(oops)
from sympy import re, im
def imaginaryEqualsReal(number):
  print(type(re(number)))
  print(im(number), I*re(number))
  return im(number), re(number)
print(answer)
image0001, real0001 = imaginaryEqualsReal(answer)
