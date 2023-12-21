
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = np.shape(matrix)
    for i in range(rows):
        for j in range(cols):
            for x in range(i, rows):
                for y in range(j, cols):
                    submat = matrix[i:x+1, j:y+1]
                    if submat.size == 175:
                        count += 1
    return count
