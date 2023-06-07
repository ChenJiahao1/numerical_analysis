import math
from time import *


#  x = fai5(x)

def f(x):  # 使用秦九韶算法减少运算次数
    coefficient = [7, -13, -21, -12, 58, 3]
    f = coefficient[0]
    for i in range(1, len(coefficient)):
        f = f * x + + coefficient[i]
    return f


def diff_f(x):
    coefficient = [35, -52, -63, -24, 58]
    f = coefficient[0]
    for i in range(1, len(coefficient)):
        f = f * x + + coefficient[i]
    return f


LIMIT = 1e-5
xlow = 1
xup = 2
xn = 1.5
tmp = 2
iter = 0

while math.fabs(xn - tmp) >= LIMIT:     # tmp 表示 x_n-1
    print("{:d} {:.5f}".format(iter, xn))
    iter += 1
    xn, tmp = xn - f(xn) / diff_f(xn), xn
print("{:d} {:.5f}".format(iter, xn))
