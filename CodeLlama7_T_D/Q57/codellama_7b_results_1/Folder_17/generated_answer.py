
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows - 1):
        for j in range(cols - 1):
            if sum(matrix[i:i+2, j:j+2]) == 398:
                submatrices.append(matrix[i:i+2, j:j+2])
    return submatrices
