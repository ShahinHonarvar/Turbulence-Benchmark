
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 76 + 1):
        for j in range(len(matrix[i]) - 76 + 1):
            if matrix[i:i+76, j:j+76].all():
                count += 1
    return count
