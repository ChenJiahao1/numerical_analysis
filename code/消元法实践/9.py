import numpy as np

A1 = np.mat([[1, 2, -2], [1, 1, 1], [2, 2, 1]])
A2 = np.mat([[2, -1, 1], [1, 1, 1], [1, 1, -2]])


def judge_convergence(B):
    eig, _ = np.linalg.eig(B)
    print(np.max(np.abs(eig)))
    if np.max(np.abs(eig)) < 1:
        return True
    else:
        return False


def solve(A):
    D = np.mat(np.diag(np.diag(A)))
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    B_j = np.dot(-D.I, L + U)
    B_s = np.dot(-(D + L).I, U)
    print('Jacobi迭代法:', judge_convergence(B_j))
    print('Gauss_Seidel迭代法:', judge_convergence(B_s))


solve(A1)
print()
solve(A2)
