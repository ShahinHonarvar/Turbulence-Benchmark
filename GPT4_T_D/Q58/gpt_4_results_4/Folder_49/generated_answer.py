
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = np.shape(matrix)
    count = 0
    for i in range(rows):
        for j in range(cols):
            for x in range(i, rows):
                for y in range(j, cols):
                    submatrix = matrix[i:x+1, j:y+1]
                    if np.size(submatrix) == 72:
                        count += 1
    return count
