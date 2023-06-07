import numpy as np

A = np.mat([[11, -3, -2], [-1, 5, -3], [-2, -12, 19]])
b = np.mat([3, 6, -7]).reshape(-1, 1)
# test_A = np.mat([[10, 3, 1], [2, -10, 3], [1, 3, 10]])
# test_b = np.mat([14, -5, 14]).reshape(-1, 1)


def judge_convergence(B):   # 利用谱半径来判断是否收敛
    eig, _ = np.linalg.eig(B)
    if np.max(abs(eig)) < 1:
        return True
    else:
        return False


def Jacobi(A, b):
    D = np.mat(np.diag(np.diag(A)))
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    B_j = np.dot(-D.I, L + U)
    g_j = np.dot(D.I, b)
    if judge_convergence(B_j):
        x = np.mat(np.zeros(shape=(A.shape[0], 1)))
        print('初始值:', x.T)
        for i in range(3):
            x = np.dot(B_j, x) + g_j
            print('第{:d}次迭代：'.format(i+1), x.T)
    else:
        print("此系数矩阵Jacobi迭代法不收敛！")


def Gauss_Seidel(A, b):
    D = np.mat(np.diag(np.diag(A)))
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    B_s = np.dot(-(D + L).I, U)
    g_s = np.dot((D + L).I, b)
    if judge_convergence(B_s):
        x = np.mat(np.zeros(shape=(A.shape[0], 1)))
        print('初始值:', x.T)
        for i in range(3):
            x = np.dot(B_s, x) + g_s
            print('第{:d}次迭代：'.format(i+1), x.T)
    else:
        print("此系数矩阵Gauss_Seidel迭代法不收敛！")


Jacobi(A, b)
print()
Gauss_Seidel(A, b)
# print(np.linalg.solve(test_A, test_b))
# Jacobi(test_A, test_b)
# print()
# Gauss_Seidel(test_A, test_b)
