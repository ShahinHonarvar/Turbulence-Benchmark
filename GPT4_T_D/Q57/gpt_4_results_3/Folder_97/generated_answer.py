
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n, m = len(matrix), len(matrix[0])
    
    for si in range(n):
        for sj in range(m):
            for ei in range(si, n):
                for ej in range(sj, m):
                    submatrix = matrix[si:ei+1, sj:ej+1]
                    if np.sum(submatrix) == -617:
                        submatrices.append(submatrix)
                    
    return submatrices
