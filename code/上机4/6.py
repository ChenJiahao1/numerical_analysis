import math
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import leastsq
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置-黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 原始的x， y值
true_x = np.array([1.0, 2.0, 4.0, 5.0])
true_y = np.array([0.33, 0.40, 0.44, 0.45])

plt.figure()
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.plot(true_x, true_y, 'k.')

# 取x， y的倒数
x = np.asarray([1 / i for i in true_x])
y = np.asarray([1 / i for i in true_y])
s0 = len(x)
s1 = sum(x)
s2 = 0
for num in x:
    s2 += num * num
t0 = sum(y)
t1 = 0
for i in range(len(x)):
    t1 += x[i]*y[i]
print(s0, s1, s2, t0, t1)
param1 = [0, 0]


# 对非线性组合模型作线性转换
def my_func(s, x):
    c0, c1 = s
    return c0 + c1 * x


# 通过拟合后得到的参数再作图
def true_func(s, x):
    c0, c1 = s
    return x / (c0 * x + c1)


# 残差
def dist(a, fun, x, y):
    return fun(a, x) - y


# 拟合
var = leastsq(dist, param1, args=(my_func, x, y))
print(var[0].round(3))
plt.plot(true_x, true_func(var[0], true_x), 'red')

plt.legend(['sample data', 'true_fun'], loc='upper left')
plt.savefig('sample.jpg')
plt.show()
