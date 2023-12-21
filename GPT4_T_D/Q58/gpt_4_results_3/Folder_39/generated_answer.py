
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            for x in range(rows - r + 1):
                for y in range(cols - c + 1):
                    if np.size(matrix[x:x + r, y:y + c]) == 59:
                        count += 1
    return count
