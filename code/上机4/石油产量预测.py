import math
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import leastsq
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置-黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

x0 = np.arange(1994, 2004, 1, dtype='float')
x = np.asarray([i-1994 for i in x0])
y = np.array([67.052, 68.008, 69.803, 72.024, 73.400, 72.063, 74.6669, 74.487, 74.065, 76.777])
plt.figure()
plt.title('世界石油产量')
plt.xlabel('年')
plt.ylabel('桶/天$(*10^6)$')
plt.grid(True)
plt.plot(x0, y, 'k.')

param1 = [0, 0]


def linear_fun(s, x):
    k, b = s
    return k * x + b


param2 = [0, 0, 0]


def quadratic_fun(s, x):
    k1, k2, b = s
    return k1 * x ** 2 + k2 * x + b


param3 = [0, 0, 0, 0]


def cubic_fun(s, x):
    k1, k2, k3, b = s
    return k1 * x ** 3 + k2 * x ** 2 + k3 * x + b


def dist(a, fun, x, y):
    return fun(a, x) - y


funs = [linear_fun, quadratic_fun, cubic_fun]
params = [param1, param2, param3]
colors = ['blue', 'red', 'black']
fun_name = ['linear_fun', 'quadratic_fun', 'cubic_fun']

for i, (func, param, color, name) in enumerate(zip(funs, params, colors, fun_name)):
    var = leastsq(dist, param, args=(func, x, y))
    print('[%s] 二范数: %.4f, abs(bias): %.4f, bias_std: %.4f' % (name,
                                                               ((y-func(var[0], x))**2).sum(),
                                                               (y-func(var[0], x)).std(),
                                                               (abs((y-func(var[0], x))).mean())))
    print(var[0])
    print(func(var[0], 2010-1994))
    plt.plot(x0, func(var[0], x), color)
plt.legend(['sample data', 'linear_fun', 'quadratic_fun', 'cubic_fun'], loc='upper left')
plt.savefig('predict.jpg')
plt.show()
