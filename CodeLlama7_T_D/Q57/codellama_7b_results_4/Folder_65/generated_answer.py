
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i in range(rows - 1):
        for j in range(cols - 1):
            sum = 0
            for k in range(3):
                for l in range(3):
                    sum += matrix[i + k, j + l]
            if sum == 78:
                result.append((i, j, i + 2, j + 2))
    return result
