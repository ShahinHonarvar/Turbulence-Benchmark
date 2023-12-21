
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for r in range(rows):
        for c in range(columns):
            for x in range(r, rows):
                for y in range(c, columns):
                    submatrix = matrix[r:x+1, c:y+1]
                    if np.size(submatrix) == 130:
                        count += 1
    return count
