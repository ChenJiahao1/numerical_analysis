import numpy as np


def Gauss(aug_matrix):
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            l = aug_matrix[i][k] / aug_matrix[k][k]
            for j in range(k + 1, n + 1):
                aug_matrix[i][j] = aug_matrix[i][j] - l * aug_matrix[k][j]
            aug_matrix[i][k] = 0

    x = np.ones(n)

    x[n - 1] = aug_matrix[n - 1][n] / aug_matrix[n - 1][n - 1]

    for k in range(n - 1, -1, -1):
        sum = 0
        for j in range(k + 1, n):
            sum += aug_matrix[k][j] * x[j]
        x[k] = (aug_matrix[k][n] - sum) / aug_matrix[k][k]
    print(np.round(x, 5))
    print('误差:', np.linalg.norm(x - x_exact, ord=np.inf) / np.linalg.norm(x_exact, ord=np.inf))


def judge_convergence(B):
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
        limit = 1e-7
        x0 = np.mat(np.zeros(shape=(A.shape[0], 1)))
        x = np.dot(B_j, x0) + g_j
        while np.min(abs(x - x0)) > limit:
            x0 = x
            x = np.dot(B_j, x) + g_j
        print(np.round(x.T, 5))
        print('误差:', np.linalg.norm(x.reshape(1, -1) - x_exact, ord=np.inf) / np.linalg.norm(x_exact, ord=np.inf))
    else:
        print("该矩阵不收敛！")


def Gauss_Seidel(A, b):
    D = np.mat(np.diag(np.diag(A)))
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    B_s = np.dot(-(D + L).I, U)
    g_s = np.dot((D + L).I, b)
    if judge_convergence(B_s):
        limit = 1e-7
        x0 = np.mat(np.zeros(shape=(A.shape[0], 1)))
        x = np.dot(B_s, x0) + g_s
        while np.min(np.fabs(x - x0)) > limit:
            x0 = x
            x = np.dot(B_s, x) + g_s
        print(np.round(x.T, 5))
        print('误差:', np.linalg.norm(x.reshape(1, -1) - x_exact, ord=np.inf) / np.linalg.norm(x_exact, ord=np.inf))
    else:
        print("该矩阵不收敛！")


nums = [2, 5, 10, 20]
for n in nums:
    print('n =', n)
    x_exact = np.ones(n).reshape(-1, 1)
    Hilbert = np.empty((n, n))
    x = np.ones(n).reshape(-1, 1)

    for i in range(0, n):
        for j in range(0, n):
            Hilbert[i][j] = 1 / (j + 1 + i)
    b = np.dot(Hilbert, x)

    # Gauss
    Gauss(np.concatenate((Hilbert, b), axis=-1))

    # 迭代法
    x = np.mat(np.ones(n).reshape(-1, 1))
    b = np.dot(Hilbert, x)
    print('Jacobi:')
    Jacobi(Hilbert, b)
    print('Gauss_Seidel:')
    Gauss_Seidel(Hilbert, b)
    print()
