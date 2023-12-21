
import numpy as np

def submatrix_with_particular_sum(matrix):
    M, N = matrix.shape
    res = []
    for size_m in range(1, M + 1):
        for size_n in range(1, N + 1):
            for x in range(M - size_m + 1):
                for y in range(N - size_n + 1):
                    submatrix = matrix[x:x+size_m, y:y+size_n]
                    
                    if submatrix.sum() == -86:
                        res.append(submatrix)
    return res
