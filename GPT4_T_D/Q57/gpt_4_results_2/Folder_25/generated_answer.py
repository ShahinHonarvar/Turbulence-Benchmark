
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    results = []

    for dim1 in range(1, m+1):
        for dim2 in range(1, n+1):
            for i in range(m-dim1+1):
                for j in range(n-dim2+1):
                    submatrix = matrix[i:i+dim1, j:j+dim2]
                    if np.sum(submatrix) == -20:
                        results.append(submatrix)
    return results
