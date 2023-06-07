import math
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置-黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


#  x = fai5(x)

def f(x):
    return pow((-58 * x - 3) / (7 * pow(x, 3) - 13 * pow(x, 2) - 21 * x - 12), 1 / 2)


LIMIT = 1e-5
xlow = 1
xup = 2
xn = 1.5
tmp = 2
iter = 0
points = []
while math.fabs(xn - tmp) >= LIMIT:  # tmp 表示 x_n-1
    print("{:d} {:.5f}".format(iter, xn))
    iter += 1
    xn, tmp = f(xn), xn
    points.append([tmp, xn])
print("{:d} {:.5f}".format(iter, xn))


i = 0
a = 0.5
x0 = np.linspace(1, 2, 100)
y0 = np.linspace(1, 2, 100)
plt.plot(x0, y0)
x1 = np.linspace(1, 2, 10000)
y1 = np.array([f(t) for t in x1])
plt.plot(x1, y1)
for x, y in points:
    plt.title("第{:d}次迭代如图所示,$X_n=${:.5f}".format(i, round(x, 5)))

    result_x = round(x, 5)
    result_y = round(y, 5)
    plt.plot([x, x], [x, y], 'g')
    plt.text(x, y, [result_x, result_y])
    plt.pause(1)
    plt.xlim(y - a, y + a)
    plt.ylim(y - a, y + a)
    plt.plot([x, y], [y, y], 'g')
    # plt.savefig('./第{}次迭代.png'.format(i))
    plt.pause(1)
    a = a / 5
    i += 1
