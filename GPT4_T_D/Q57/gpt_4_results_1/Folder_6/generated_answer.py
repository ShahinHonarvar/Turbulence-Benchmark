
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for size_row in range(1, rows+1):
        for size_col in range(1, cols+1):
            for i in range(rows - size_row + 1):
                for j in range(cols - size_col + 1):
                    submatrix = matrix[i:i+size_row, j:j+size_col]
                    if np.sum(submatrix) == 126:
                        result.append(submatrix)
    return result
