
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 67:
                for x in range(i, rows):
                    for y in range(j, cols):
                        submatrix = matrix[i:x+1, j:y+1]
                        if np.sum(submatrix) == 67:
                            count += 1
    return count
