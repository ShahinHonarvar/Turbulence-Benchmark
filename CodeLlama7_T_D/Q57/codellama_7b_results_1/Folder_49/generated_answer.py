
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            if sum(matrix[i:i + 2, j:j + 2]) == -42:
                result.append((i, j, i + 2, j + 2))
    return result
