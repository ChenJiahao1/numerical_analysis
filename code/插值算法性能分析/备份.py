import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate
import pylab as pl
from scipy.interpolate import lagrange

plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置-黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

x = np.linspace(-5, 5, 21)
y1 = [-0.1923, -0.2118, -0.2353, -0.2642, -0.3, -0.3448, -0.4000, -0.4615, -0.5000, -0.4000, 0,
      0.4000, 0.5000, 0.4615, 0.4000, 0.3448, 0.3000, 0.2642, 0.2353, 0.2118, 0.1923]
y2 = [0.0016, 0.002, 0.0025, 0.0033, 0.0044, 0.0064, 0.0099, 0.0175, 0.0385, 0.1379, 1.0000,
      0.1379, 0.0385, 0.0175, 0.0099, 0.0064, 0.0044, 0.0033, 0.0025, 0.0020, 0.0016]
find = [-3.75, 0.25]

data1 = []
for i in range(len(x)):
    data1.append([x[i], y1[i]])

data2 = []
for i in range(len(x)):
    data2.append([x[i], y2[i]])


# 拉格朗日
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
                af *= (1.0 * (testdata - data_x[j]) / (data_x[i] - data_x[j]))
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
    plt.title('拉格朗日插值法' + str(cnt))
    plt.savefig('Lg' + str(cnt) + '.jpg')
    plt.show()


# 分段线性插值
def DivideLine(data, testdata):
    data_x = [data[i][0] for i in range(len(data))]
    data_y = [data[i][1] for i in range(len(data))]

    if testdata in data_x:
        return data_y[data_x.index(testdata)]
    else:
        index = 0
        for j in range(len(data_x)):
            if data_x[j] < testdata < data_x[j + 1]:
                index = j
                break
        predict = 1.0 * (testdata - data_x[index]) * \
                  (data_y[index + 1] - data_y[index]) / (data_x[index + 1] - data_x[index]) + data_y[index]
        return predict


def plot_DL(data, nums, cnt):
    data_x = [data[i][0] for i in range(len(data))]
    data_y = [data[i][1] for i in range(len(data))]

    X = np.linspace(min(data_x), max(data_x), nums)
    Y = [DivideLine(data, x) for x in X]

    # print('数据' + str(cnt) + ':')
    # for i in find:
    #     print(i, Y[X.tolist().index(i)])

    plt.plot(X, Y, label='result')

    for i in range(len(data_x)):
        plt.plot(data_x[i], data_y[i], 'ro', label='point')

    plt.xlabel('横坐标')
    plt.ylabel('纵坐标')
    plt.title('分段线性插值法' + str(cnt))
    plt.savefig('DL' + str(cnt) + '.jpg')
    plt.show()


# 牛顿插值
def calF(data):
    data_x = [data[i][0] for i in range(len(data))]
    data_y = [data[i][1] for i in range(len(data))]

    F = [1 for _ in range(len(data))]
    FM = []
    for i in range(len(data)):
        FME = []
        if i == 0:
            FME = data_y
        else:
            for j in range(len(FM[len(FM) - 1]) - 1):
                delta = data_x[i + j] - data_x[j]
                value = 1.0 * (FM[len(FM) - 1][j + 1] - FM[len(FM) - 1][j]) / delta
                FME.append(value)
        FM.append(FME)
    F = [fme[0] for fme in FM]
    # print(FM)
    return F


def NT(data, testdata, F):
    predict = 0
    data_x = [data[i][0] for i in range(len(data))]
    data_y = [data[i][1] for i in range(len(data))]
    if testdata in data_x:
        return data_y[data_x.index(testdata)]
    else:
        for i in range(len(data_x)):
            Eq = 1
            if i != 0:
                for j in range(i):
                    Eq = Eq * (testdata - data_x[j])
                predict += (F[i] * Eq)
    return predict


def plot_NT(data, nums, cnt):
    data_x = [data[i][0] for i in range(len(data))]
    data_y = [data[i][1] for i in range(len(data))]

    X = np.linspace(min(data_x), max(data_x), nums)

    F = calF(data)
    Y = [NT(data, x, F) for x in X]

    plt.plot(X, Y, label='result')
    for i in range(len(data_x)):
        plt.plot(data_x[i], data_y[i], 'ro', label='point')

    plt.xlabel('横坐标')
    plt.ylabel('纵坐标')
    plt.title('牛顿多项式插值法' + str(cnt))
    plt.savefig('NT' + str(cnt) + '.jpg')
    plt.show()


# 样条插值
def interpolate_b_spline(x, y, x_new, der=0):
    """ B 样条曲线插值 或者导数. 默认der = 0"""
    tck = interpolate.splrep(x, y)
    y_bspline = interpolate.splev(x_new, tck, der=der)
    return y_bspline


def func1(x):
    return x / (1 + x * x)


def func2(x):
    return 1 / (1 + 25 * x * x)


plot_Lg(data1, 1000, 1)
plot_Lg(data2, 1000, 2)

plot_NT(data1, 1000, 1)
plot_NT(data2, 1000, 2)

plot_DL(data1, 1000, 1)
plot_DL(data2, 1000, 2)

print('拉格朗日插值法:')
print('数据1:')
print(Lg(data1, -3.75), Lg(data1, 0.25))
print('R(-3.75)=', func1(-3.75) - Lg(data1, -3.75))
print('R(0.25)=', func1(0.25) - Lg(data1, 0.25))

print('数据2:')
print(Lg(data2, -3.75), Lg(data2, 0.25))
print('R(-3.75)=', func2(-3.75) - Lg(data2, -3.75))
print('R(0.25)=', func2(0.25) - Lg(data2, 0.25))

print()

print('牛顿多项式插值法:')
F1 = calF(data1)
F2 = calF(data2)
print('数据1:')
print(NT(data1, -3.75, F1), NT(data1, 0.25, F1))
print('R(-3.75)=', func1(-3.75) - NT(data1, -3.75, F1))
print('R(0.25)=', func1(0.25) - NT(data1, 0.25, F1))

print('数据2:')
print(NT(data2, -3.75, F2), NT(data2, 0.25, F2))
print('R(-3.75)=', func2(-3.75) - NT(data2, -3.75, F2))
print('R(0.25)=', func2(0.25) - NT(data2, 0.25, F2))

print()

print('分段线性插值法:')
print('数据1:')
print(DivideLine(data1, -3.75), DivideLine(data1, 0.25))
print('R(-3.75)=', func1(-3.75) - DivideLine(data1, -3.75))
print('R(0.25)=', func1(0.25) - DivideLine(data1, 0.25))

print('数据2:')
print(DivideLine(data2, -3.75), DivideLine(data2, 0.25))
print('R(-3.75)=', func2(-3.75) - DivideLine(data2, -3.75))
print('R(0.25)=', func2(0.25) - DivideLine(data2, 0.25))

print()

cnt = 1
print('样条插值法:')
print('数据1:')
y_new = interpolate_b_spline(x, y1, find)
print(*y_new)
print('R(-3.75)=', func1(-3.75) - y_new[0])
print('R(0.25)=', func1(0.25) - y_new[1])
x_new = np.linspace(-5, 5, 1000)
y_new = interpolate_b_spline(x, y1, x_new)
plt.plot(x_new, y_new)
plt.xlabel('横坐标')
plt.ylabel('纵坐标')
plt.title('样条插值插值法' + str(cnt))
plt.savefig('spline' + str(cnt) + '.jpg')
plt.show()

cnt = 2
print('数据2:')
y_new = interpolate_b_spline(x, y2, find)
print(*y_new)
print('R(-3.75)=', func2(-3.75) - y_new[0])
print('R(0.25)=', func2(0.25) - y_new[1])
x_new = np.linspace(-5, 5, 1000)
y_new = interpolate_b_spline(x, y2, x_new)
plt.plot(x_new, y_new)
plt.xlabel('横坐标')
plt.ylabel('纵坐标')
plt.title('样条插值插值法' + str(cnt))
plt.savefig('spline' + str(cnt) + '.jpg')
plt.show()
print()

for x in find:
    print(x, func1(x), end=' ')
print()
for x in find:
    print(x, func2(x), end=' ')
