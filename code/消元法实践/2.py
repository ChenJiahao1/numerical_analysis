import copy
import math

aug_matrix = [[2.51, 1.48, 4.53, 0.05], [1.48, 0.93, -1.3, 1.03], [2.68, 3.04, -1.48, -0.53]]
# aug_matrix = [[2, -1, 3, 1], [4, 2, 5, 4], [1, 2, 0, 7]]
# n * m
n = len(aug_matrix)
m = n + 1

tmp = copy.deepcopy(aug_matrix)

# Gauss消去法解方程组
for k in range(0, n - 1):
    for i in range(k + 1, n):
        l = round(aug_matrix[i][k] / aug_matrix[k][k], 3)
        for j in range(k + 1, n + 1):
            aug_matrix[i][j] = round(aug_matrix[i][j] - l * aug_matrix[k][j], 3)
        aug_matrix[i][k] = 0

for a in aug_matrix:
    print(a)
print()
x = [0.0] * n

x[n - 1] = aug_matrix[n - 1][n] / aug_matrix[n - 1][n - 1]

for k in range(n - 1, -1, -1):
    sum = 0
    for j in range(k + 1, n):
        sum += aug_matrix[k][j] * x[j]
    x[k] = round((aug_matrix[k][n] - sum) / aug_matrix[k][k], 3)
print(x)
print()


''''''''''''''''''''''''''''''''''''''
# 列主元Gauss消去法解方程组
aug_matrix = copy.deepcopy(tmp)


def swap(k, n):
    global aug_matrix
    ans = -1
    maxn = -1
    for i in range(k, n):
        if ans < math.fabs(aug_matrix[i][k]):
            ans = math.fabs(aug_matrix[i][k])
            maxn = i
    if maxn == k:
        return
    aug_matrix[k][k::], aug_matrix[maxn][k::] = aug_matrix[maxn][k::], aug_matrix[k][k::]


for k in range(0, n - 1):
    swap(k, n)
    for i in range(k + 1, n):
        l = round(aug_matrix[i][k] / aug_matrix[k][k], 3)
        for j in range(k + 1, n + 1):
            aug_matrix[i][j] = round(aug_matrix[i][j] - l * aug_matrix[k][j], 3)
        aug_matrix[i][k] = 0

for a in aug_matrix:
    print(a)
print()
x = [0.0] * n

x[n - 1] = aug_matrix[n - 1][n] / aug_matrix[n - 1][n - 1]

for k in range(n - 1, -1, -1):
    sum = 0
    for j in range(k + 1, n):
        sum += aug_matrix[k][j] * x[j]
    x[k] = round((aug_matrix[k][n] - sum) / aug_matrix[k][k], 3)
print(x)
