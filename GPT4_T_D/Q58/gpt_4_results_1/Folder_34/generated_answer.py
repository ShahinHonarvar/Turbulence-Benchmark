
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0 
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for x in range(r, rows):
                for y in range(c, cols):
                    submatrix = matrix[r:x+1, c:y+1]
                    if np.size(submatrix) == 83:
                        count += 1
    return count
