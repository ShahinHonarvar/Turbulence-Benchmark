
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape[0], matrix.shape[1]
    submatrices_sum_minus_81 = []

    for size in range(1, min(m, n) + 1):  
        for row in range(0, m - size + 1): 
            for col in range(0, n - size + 1): 
                submatrix = matrix[row:row + size, col:col + size]
                if np.sum(submatrix) == -81:
                    submatrices_sum_minus_81.append(submatrix)

    return submatrices_sum_minus_81
