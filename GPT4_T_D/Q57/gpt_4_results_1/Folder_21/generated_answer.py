
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for sub_m in range(m):
        for sub_n in range(n):
            for i in range(m-sub_m+1):
                for j in range(n-sub_n+1):
                    submat = matrix[i:i+sub_m, j:j+sub_n]
                    if submat.sum() == -936:
                        submatrices.append(submat)
    return submatrices
