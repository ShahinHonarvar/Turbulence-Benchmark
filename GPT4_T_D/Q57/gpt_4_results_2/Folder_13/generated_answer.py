
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    results = []
    
    # consider all sub-arrays
    for si in range(m):
        for sj in range(n):
            for ei in range(si, m):
                for ej in range(sj, n):
                    if matrix[si:ei+1,sj:ej+1].sum() == 382:
                        results.append(matrix[si:ei+1,sj:ej+1])
    return results
