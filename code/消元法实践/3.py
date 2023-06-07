import copy
import math

aug_matrix = [[1, 2, 1, -2, 4], [2, 5, 3, -2, 7], [-2, -2, 3, 5, -1], [1, 3, 2, 3, 0]]
tmp = copy.deepcopy(aug_matrix)
n = len(aug_matrix)


# 列主元Gauss-Jordan消去法
def swap(k, n):
    global aug_matrix
    ans = -1
    maxn = -1
    for i in range(k, n):
        if ans < math.fabs(aug_matrix[i][k]):
            ans = math.fabs(aug_matrix[i][k])
            maxn = i
    if maxn != k:
        aug_matrix[k][k::], aug_matrix[maxn][k::] = aug_matrix[maxn][k::], aug_matrix[k][k::]
    l = aug_matrix[k][k]
    for j in range(k, n + 1):
        aug_matrix[k][j] /= l


for k in range(0, n):
    swap(k, n)
    for i in range(0, n):
        if i == k:
            continue
        l = round(aug_matrix[i][k] / aug_matrix[k][k], 3)
        for j in range(k + 1, n + 1):
            aug_matrix[i][j] = round(aug_matrix[i][j] - l * aug_matrix[k][j], 3)
        aug_matrix[i][k] = 0

for a in aug_matrix:
    print(a)
print()

x = [0.0] * n

for i in range(n):
    x[i] = aug_matrix[i][n]
print('列主元Gauss-Jordan消去法:')
print(x)


''''''''''''''''''''''''''''''''''''''
# LU分解法解方程组
aug_matrix = copy.deepcopy(tmp)
L = [[0.0] * n for _ in range(n)]
for k in range(n-1):
    for i in range(k+1, n):
        L[i][k] = aug_matrix[i][k] / aug_matrix[k][k]
        for j in range(n):
            aug_matrix[i][j] = aug_matrix[i][j] - L[i][k] * aug_matrix[k][j]
for i in range(n):
    L[i][i] = 1.0

# 求 y
y = [0.0] * n
y[0] = aug_matrix[0][n]
for i in range(1, n):
    y[i] = aug_matrix[i][n]
    for j in range(i):
        y[i] = y[i] - L[i][j] * y[j]
# print(y)

# aug_matrix 为ux=y 的增广矩阵
for i in range(n):
    aug_matrix[i][n] = y[i]

for a in aug_matrix:
    print(a)
print()
# 求x
x = [0.0] * n
x[n - 1] = aug_matrix[n - 1][n] / aug_matrix[n - 1][n - 1]

for k in range(n - 1, -1, -1):
    sum = 0
    for j in range(k + 1, n):
        sum += aug_matrix[k][j] * x[j]
    x[k] = round((aug_matrix[k][n] - sum) / aug_matrix[k][k], 3)
print('LU分解法解方程组:')
print(x)
print()