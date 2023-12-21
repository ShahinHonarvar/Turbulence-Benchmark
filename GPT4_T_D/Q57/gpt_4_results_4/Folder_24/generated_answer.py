
import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    result_submatrices = []
    for i in range(n):
        for j in range(m):
            for _n in range(i+1, n+1):
                for _m in range(j+1, m+1):
                    submatrix = matrix[i:_n, j:_m]
                    if np.sum(submatrix) == -36:
                        result_submatrices.append(submatrix.tolist())
    return result_submatrices
