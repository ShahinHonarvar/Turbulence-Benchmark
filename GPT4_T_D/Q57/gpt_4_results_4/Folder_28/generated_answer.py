
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for row1 in range(m):
        for row2 in range(row1+1, m+1):
            for col1 in range(n):
                for col2 in range(col1+1, n+1):
                    submatrix = matrix[row1:row2, col1:col2]
                    if np.sum(submatrix) == 15:
                        submatrices.append(submatrix)
                        
    if len(submatrices) == 0: 
        return []
        
    return submatrices
