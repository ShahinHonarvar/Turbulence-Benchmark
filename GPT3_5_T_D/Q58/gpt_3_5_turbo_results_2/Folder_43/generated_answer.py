
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            for r in range(i, m):
                for c in range(j, n):
                    submatrix = matrix[i:r+1, j:c+1]
                    if np.sum(submatrix) == 85 * (r-i+1) * (c-j+1):
                        count += 1

    return count
