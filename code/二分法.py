import math
from time import *

LIMIT = 1e-5
xlow = 1
xup = 2

startT = time()  # 记录起始时间


def f(x):  # 使用秦九韶算法减少运算次数
    coefficient = [7, -13, -21, -12, 58, 3]
    f = coefficient[0]
    for i in range(1, len(coefficient)):
        f = f * x + + coefficient[i]
    return f


def sign(x):
    if x == 0:
        return 0
    return int(math.copysign(1, x))



iter = 0
xn = 2
tmp = 1
while math.fabs(xn - tmp) >= LIMIT:
    xmid = xlow + (xup - xlow) / 2
    xn, tmp = xmid, xn
    print("{:d} {:.5f}".format(iter, xmid))
    iter += 1
    if sign(f(xmid)) * sign(f(xlow)) < 0:
        xup = xmid
    else:
        xlow = xmid