import math
from time import *


#  x = fai5(x)

def f(x):
    return pow((-58 * x - 3) / (7 * pow(x, 3) - 13 * pow(x, 2) - 21 * x - 12), 1 / 2)


def aitken(xn, tmp1, tmp2):     # 用于计算aitken数列
    return tmp2 - pow((tmp1 - tmp2), 2) / (xn - 2 * tmp1 + tmp2)


LIMIT = 1e-5
xlow = 1
xup = 2
xn = 1.5
tmp1 = 2
tmp2 = 2
iter = 0

while math.fabs(xn - tmp1) >= LIMIT:  # tmp1 表示 x_n-1    tmp2 表示 x_n-2
    print("{:d} {:.5f}".format(iter, xn))
    if iter == 0:
        xn, tmp1 = f(xn), xn
    else:
        xn, tmp1, tmp2 = f(xn), xn, tmp1
        xn = aitken(xn, tmp1, tmp2)
    iter += 1
print("{:d} {:.5f}".format(iter, xn))
