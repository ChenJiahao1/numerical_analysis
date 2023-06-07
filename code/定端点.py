import math
from time import *


#  x = fai5(x)

def f(x):  # 使用秦九韶算法减少运算次数
    coefficient = [7, -13, -21, -12, 58, 3]
    f = coefficient[0]
    for i in range(1, len(coefficient)):
        f = f * x + + coefficient[i]
    return f


LIMIT = 1e-5
x0 = 1
xn = 2
tmp = 1.5
iter = 1
print("{:d} {:.5f}".format(0, 1))
while math.fabs(xn - tmp) >= LIMIT:     # tmp 表示 x_n-1
    print("{:d} {:.5f}".format(iter, xn))
    iter += 1
    xn, tmp = xn - ((xn - x0) / (f(xn) - f(x0))) * f(xn), xn
print("{:d} {:.5f}".format(iter, xn))
