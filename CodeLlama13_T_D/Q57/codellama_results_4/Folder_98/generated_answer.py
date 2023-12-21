
import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    for i in range(n):
        for j in range(m):
            if matrix[i,j] == 0:
                continue
            for k in range(i+1, n):
                for l in range(j+1, m):
                    if (matrix[k,l] - matrix[i,j]) % matrix[i,j] == 0:
                        return [matrix[i:k+1, j:l+1]]
    return []
