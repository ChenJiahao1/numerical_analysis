import numpy as np

A = np.array([[10, 7, 8, 7], [7, 5, 6, 5], [8, 6, 10, 9], [7, 5, 9, 10]], dtype=float)

b1 = np.array([32, 23, 33, 31])
b2 = np.array([32.1, 22.9, 33.1, 30.9])

result1 = np.linalg.solve(A, b1)
print(result1)
result2 = np.linalg.solve(A, b2)
print(result2)

# 解与准确解的相对误差
mis_result = result2 - result1
print(np.linalg.norm(mis_result, ord=np.inf) / np.linalg.norm(result1, ord=np.inf))
print(np.linalg.norm(mis_result, ord=1) / np.linalg.norm(result1, ord=1))


# 扰动方程的右端项和原右端项的相对误差
mis_b = b2 - b1
print(np.linalg.norm(mis_b, ord=np.inf) / np.linalg.norm(b1, ord=np.inf))
print(np.linalg.norm(mis_b, ord=1) / np.linalg.norm(b1, ord=1))
