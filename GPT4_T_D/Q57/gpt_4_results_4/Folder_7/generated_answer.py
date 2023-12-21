
import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    
    for left in range(n):
        for up in range(m):
            for right in range(left + 1, n + 1):
                for down in range(up + 1, m + 1):
                    submatrix = matrix[up:down, left:right]
                    if np.sum(submatrix) == -128:
                        submatrices.append(submatrix)
                        
    return submatrices
