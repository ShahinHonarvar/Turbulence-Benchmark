
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            for x in range(rows - i + 1):
                for y in range(cols - j + 1):
                    if np.size(matrix[x:x+i, y:y+j]) == 118:
                        count += 1
    return count
