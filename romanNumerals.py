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

tF = E**-pi
sF = I**4
s = speedOfSpace()
t = speedOfTime()
sE = s**sF
sI = s**tF
tE = t**tF
tI = t**sF

def negHalf():
    return E**(sE**2 + tI**2)**I
  
def half():
    return E**(sE**2 - tI**2)**I

def sqRt_Neg_Half():
    return E**(tE**2 - sI**2)**I

def sqRt_Pos_Half():
    return E**(tE**2 - sI**2)**I

def zero():
    return (E**two() + sqRt_Pos_Half()) - (E**half() + sqRt_Neg_Half())

def sqRt_3rd_derivative_light():
    return sE + tE

def infinity_Light():
    return sE * tE

def infinity_complex():
    return sE * tE**-(I**4)

def infinity_Zero():
    return sE * tE**-(I**2)

def infinity_real():
    return  E**sE + tE

def infinity_Light():
    return  E**sE  tE

def infinity_E():
    return
