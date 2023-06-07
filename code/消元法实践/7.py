import math
from math import inf
import numpy as np

A = np.array([[-2, 1, 0, 0], [1, -2, 1, 0], [0, 1, -2, 1], [0, 0, 1, -2]])

# inf 范数
norm_inf = 0
for i in range(A.shape[0]):
    tmp = 0
    for j in range(A.shape[1]):
        tmp += abs(A[i][j])
    if tmp > norm_inf:
        norm_inf = tmp
print(norm_inf)
# print(np.linalg.norm(A, ord=inf))

# 1 范数
norm_1 = 0
for j in range(A.shape[1]):
    tmp = 0
    for i in range(A.shape[0]):
        tmp += abs(A[i][j])
    if tmp > norm_1:
        norm_1 = tmp
print(norm_1)
# print(np.linalg.norm(A, ord=1))

# 2 范数
eig, eig_vector = np.linalg.eig(np.dot(A.T, A))    # 特征值， 特征向量
norm_2 = math.sqrt(max(eig))
print(norm_2)
# print(np.linalg.norm(A, ord=2))

# Cond(A)_2
CondA = math.sqrt(max(eig)) / math.sqrt(min(eig))
print(CondA)