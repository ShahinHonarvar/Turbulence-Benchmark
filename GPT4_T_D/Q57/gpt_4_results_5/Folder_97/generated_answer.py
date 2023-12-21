
import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    submatrices = []
    for x1 in range(n):
        for y1 in range(m):
            for x2 in range(x1, n):
                for y2 in range(y1, m):
                    subm = matrix[x1:x2+1, y1:y2+1]
                    if subm.sum() == -617:
                        submatrices.append(subm)
    return submatrices
