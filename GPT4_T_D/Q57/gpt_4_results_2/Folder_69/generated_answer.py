
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    for row_size in range(1, rows + 1):
        for col_size in range(1, cols + 1):
            for r in range(rows - row_size + 1):
                for c in range(cols - col_size + 1):
                    sub_matrix = matrix[r:r+row_size, c:c+col_size]
                    if np.sum(sub_matrix) == 752:
                        result.append(sub_matrix)
    
    return result
