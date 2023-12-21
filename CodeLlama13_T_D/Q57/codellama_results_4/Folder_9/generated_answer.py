
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for i in range(row, rows):
                for j in range(col, cols):
                    if np.sum(matrix[row:i+1, col:j+1]) == -86:
                        return matrix[row:i+1, col:j+1]
    return []
