
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 13 + 1):
        for j in range(len(matrix[i]) - 13 + 1):
            if sum(matrix[i:i+13, j:j+13].flatten()) == 13:
                count += 1
    return count
