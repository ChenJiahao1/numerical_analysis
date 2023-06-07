import math
from time import *


#  x = fai5(x)

def f(x):
    return pow((-58 * x - 3) / (7 * pow(x, 3) - 13 * pow(x, 2) - 21 * x - 12), 1 / 2)


def steffensen(x):
    t = f(x)
    return x - pow((t - x), 2) / (f(t) - 2 * t + x)


LIMIT = 1e-5
xlow = 1
xup = 2
xn = 1.5
tmp = 2
iter = 0

while math.fabs(xn - tmp) >= LIMIT:  # tmp 表示 x_n-1
    print("{:d} {:.6g}".format(iter, xn))
    iter += 1
    xn, tmp = steffensen(xn), xn
print("{:d} {:.6g}".format(iter, xn))
