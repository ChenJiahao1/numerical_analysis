from sympy import symbols, expand
import numpy as np
from scipy.interpolate import lagrange

# 拉格朗日插值
x = np.array([0, 1, 2])
y = np.array([1, 2, 3])
poly = lagrange(x, y)
print(poly)

x = np.array([1, 3, 4, 7])
y = np.array([0, 2, 15, 12])
poly = lagrange(x, y)
print(poly)

print()

# 牛顿多项式插值
dp1 = [1, 1, 0]  # 差商表1
dp2 = [0, 1, 4, -1.25]  # 差商表2
x = symbols('x')
phi = dp1[0] + dp1[1] * (x - 0) + dp1[2] * (x - 0) * (x - 1)
print(expand(phi))
phi = dp2[0] + dp2[1] * (x - 1) + dp2[2] * (x - 1) * (x - 3) + dp2[3] * (x - 1) * (x - 3) * (x - 4)
print(expand(phi))
