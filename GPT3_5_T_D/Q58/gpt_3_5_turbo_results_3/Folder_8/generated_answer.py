
import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 29
    count = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for r in range(i, len(matrix)):
                for c in range(j, len(matrix[0])):
                    submatrix = matrix[i:r+1, j:c+1]
                    if np.sum(submatrix) == n:
                        count += 1
    return count
