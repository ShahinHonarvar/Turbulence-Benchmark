
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    
    for sub_m_size in range(1, m+1):
        for sub_n_size in range(1, n+1):
            for i in range(m - sub_m_size + 1):
                for j in range(n - sub_n_size + 1):
                    submatrix = matrix[i: i+sub_m_size, j: j+sub_n_size]
                    if np.sum(submatrix) == 64:
                        submatrices.append(submatrix)
    return submatrices
