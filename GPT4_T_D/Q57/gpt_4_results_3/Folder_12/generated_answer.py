
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    
    for window_size in range(1, min(m, n) + 1):
        for x in range(m - window_size + 1):
            for y in range(n - window_size + 1):
                submatrix = matrix[x:x+window_size, y:y+window_size]
                if submatrix.sum() == -83:
                    submatrices.append(submatrix)
                    
    return submatrices
