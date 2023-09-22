#wyznaczanie wartosci pierwiastka metodą herona - newtona/raphsona
# https://www.youtube.com/watch?v=C_FFlau09_8
import math
def pierw(pole,eps):
    a=1
    b=pole
    while math.fabs(a-b)>=eps:
        a=(a+b)/2
        b=pole/a
    return (a+b)/2
print(pierw(3,0.001))