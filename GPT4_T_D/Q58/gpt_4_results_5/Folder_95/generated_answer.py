
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for x1 in range(rows):
        for x2 in range(x1 + 1, rows + 1):
            for y1 in range(cols):
                for y2 in range(y1 + 1, cols + 1):
                    if np.size(matrix[x1:x2, y1:y2]) == 87:
                        count += 1
    return count
