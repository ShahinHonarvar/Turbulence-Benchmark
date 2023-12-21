
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = np.shape(matrix)
    for x1 in range(rows):
        for y1 in range(cols):
            for x2 in range(x1, rows):
                for y2 in range(y1, cols):
                    submatrix = matrix[x1:x2+1, y1:y2+1]
                    if submatrix.size == 122:
                        count += 1
    return count
