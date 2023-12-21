
import numpy as np

def submatrix_with_particular_sum(mat):
    result = []
    rows, cols = mat.shape
    for row_size in range(1, rows + 1):
        for col_size in range(1, cols + 1):
            for row in range(0, rows - row_size + 1):
                for col in range(0, cols - col_size + 1):
                    submat = mat[row:row+row_size, col:col+col_size]
                    if np.sum(submat) == 901:
                        result.append(submat)
    return result
