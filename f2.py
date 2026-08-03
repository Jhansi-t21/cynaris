import numpy as np


# 1. Broadcasting
print("1. Broadcasting")
arr = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr)

broadcast_result = arr + 10
print("After Broadcasting (+10):", broadcast_result)

# 2. Vectorized Operations
print("\n2. Vectorized Operations")

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print("Array A:", a)
print("Array B:", b)

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# 3. Matrix Multiplication
print("\n3. Matrix Multiplication")

matrix1 = np.array([[1, 2],
                    [3, 4]])

matrix2 = np.array([[5, 6],
                    [7, 8]])

print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)

result = np.matmul(matrix1, matrix2)

print("Result of Matrix Multiplication:\n", result)