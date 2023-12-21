
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for sub_m in range(m+1):
        for sub_n in range(n+1):
            for row in range(m-sub_m+1):
                for col in range(n-sub_n+1):
                    submatrix = matrix[row:row+sub_m, col:col+sub_n]
                    if np.sum(submatrix) == 84:
                        submatrices.append(submatrix)
    return submatrices
