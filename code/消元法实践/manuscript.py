import numpy as np

A = np.mat([[10, 3, 1], [2, -10, 3], [1, 3, 10]])
b = np.mat([14, -5, 14]).reshape(-1, 1)


def judge_convergence(B):
    eig, _ = np.linalg.eig(B)
    if np.max(eig) < 1:
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
        limit = 1e-5
        x0 = np.mat(np.zeros(shape=(A.shape[0], 1)))
        x = np.dot(B_j, x0) + g_j
        while np.min(np.fabs(x - x0)) > limit:
            x0 = x
            x = np.dot(B_j, x) + g_j
        print(x)
    else:
        print("该矩阵不收敛！")


Jacobi(A, b)
