from sympy import I, pi, E, log

o = (E**(pi) + E**(I*pi)) + (E**(pi) - E**(I*pi))
i = E**I**o**pi
v = i**o
x = v**(i**o)
l = x**(v**(i**o))
c = l**(x**(v**(i**o)))
m = c**(l**(x**(v**(i**o))))

x = (m**2 + m**2) + (m**2 - m**2)
y = (m**2 + m**2) - (m**2 - m**2)

def one():
    return (x / y)

def zero():
    return (x - y)

def speedOfTime():
    return  (m**2 - m**2)**(1/2)

def speedOfSpace():
    return  (m**2 + m**2)**(1/2)
# print(c**(one() + one() + one() + one()))
print(speedOfSpace()**(E**(pi)) + speedOfTime()**(E**(I**4)))