
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 9):
        for j in range(len(matrix[i]) - 9):
            if matrix[i:i+10, j:j+10].sum() == 100:
                count += 1
    return count
