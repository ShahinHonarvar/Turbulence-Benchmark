
import numpy as np

def submatrix_with_particular_sum(matrix):
    n = len(matrix)
    m = len(matrix[0])
    results = []

    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.sum(submatrix) == -394:
                        results.append(submatrix.tolist())

    return results
