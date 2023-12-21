
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = np.shape(matrix)
    result = []

    for row_len in range(1, rows + 1):
        for col_len in range(1, cols + 1):
            for row in range(rows - row_len + 1):
                for col in range(cols - col_len + 1):
                    submatrix = matrix[row:row + row_len, col:col + col_len]
                    if np.sum(submatrix) == 398:
                        result.append(submatrix.tolist())
                        
    return result
