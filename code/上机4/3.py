import numpy as np

A = np.mat([[2, 3, 1, 2], [4, -5, 2, 1]])
b = np.mat([11, 3, 6, 7])
tmp = A
A = np.dot(A, A.T)
b = np.dot(tmp, b.T)
print(A)
print(b)
x = np.linalg.solve(A, b)
print(x)

A = np.mat([[1, 1, 1, 1, 1], [-2, -1, 0, 1, 2], [4, 1, 0, 1, 4]])
b = np.mat([0, 1, 2, 1, 0])
tmp = A
A = np.dot(A, A.T)
b = np.dot(tmp, b.T)
print(A)
print(b)
x = np.linalg.solve(A, b)
print(x)