
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    m,n = matrix.shape
    for sub_m in range(m):
        for sub_n in range(n):
            for i,j in np.ndindex((m-sub_m, n-sub_n)):
                submatrix = matrix[i:i+sub_m+1, j:j+sub_n+1]
                if submatrix.sum() == -336:
                    result.append(submatrix)
    return result
