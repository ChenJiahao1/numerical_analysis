import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import lagrange

plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置-黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


def func1(x):
    return x * x + 4 * x - 7


def func2(x):
    return -2 * x * x * x + 5 * x * x + x - 2


def Lg(data, testdata):
    predict = 0
    data_x = [data[i][0] for i in range(len(data))]
    data_y = [data[i][1] for i in range(len(data))]
    if testdata in data_x:
        return data_y[data_x.index(testdata)]
    for i in range(len(data_x)):
        af = 1
        for j in range(len(data_x)):
            if j != i:
                af *= ((1.0 * (testdata - data_x[j])) / (data_x[i] - data_x[j]))
        predict += data_y[i] * af
    return predict


def plot_Lg(data, nums, cnt):
    data_x = [data[i][0] for i in range(len(data))]
    data_y = [data[i][1] for i in range(len(data))]

    X = np.linspace(min(data_x), max(data_x), nums)
    Y = [Lg(data, x) for x in X]

    plt.plot(X, Y, label='result')
    for i in range(len(data_x)):
        plt.plot(data_x[i], data_y[i], 'ro', label='point')

    plt.xlabel('横坐标')
    plt.ylabel('纵坐标')
    plt.title('拉格朗日插值法')
    plt.savefig('point' + str(cnt) + '.jpg')
    plt.show()


point1 = [0, 1, 2]
point2 = [0, 1, 2, 3]

cnt = 1
data1 = [[x, func1(x)] for x in point1]
nums = 1001
x = np.linspace(min(point1), max(point1), nums)
y = [func1(a) for a in x]
plt.plot(x, y)
plt.xlabel('横坐标')
plt.ylabel('纵坐标')
plt.title('$x^2 + 4x -7$')
plt.savefig('f(x)' + str(cnt) + '.jpg')
plt.show()

# 展示拉格朗日插值函数
plot_Lg(data1, nums, cnt)

# 输出多项式函数
x = np.array([0, 1, 2])
y = x * x + 4 * x - 7
poly = lagrange(x, y)
print(poly)

cnt = 2
data2 = [[x, func2(x)] for x in point2]
nums = 1001
x = np.linspace(min(point2), max(point2), nums)
y = [func2(a) for a in x]
plt.plot(x, y)
plt.xlabel('横坐标')
plt.ylabel('纵坐标')
plt.title('$-2x^3+5x^2+x-2$')
plt.savefig('f(x)' + str(cnt) + '.jpg')
plt.show()

# 展示拉格朗日插值函数
plot_Lg(data2, nums, cnt)

# 输出多项式函数
x = np.array([0, 1, 2, 3])
y = -2 * x * x * x + 5 * x * x + x - 2
poly = lagrange(x, y)
print(poly)