 
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape

    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 1:
                for r in range(i, rows):
                    for c in range(j, cols):
                        submatrix = matrix[i:r+1, j:c+1]
                        if np.sum(submatrix) == submatrix.size:
                            count += 1

    return count
