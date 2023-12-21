
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    for i in range(m-1):
        for j in range(n-1):
            sum_row = 0
            for k in range(j+1, n):
                sum_row += matrix[i][k]
            if sum_row == 41:
                return [matrix[i][j:k]]
    return []
