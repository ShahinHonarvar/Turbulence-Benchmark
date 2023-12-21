
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for row_len in range(1, rows + 1):
        for col_len in range(1, cols + 1):
            for i in range(rows - row_len + 1):
                for j in range(cols - col_len + 1):
                    submat = matrix[i: (i + row_len), j: (j + col_len)]
                    if np.sum(submat) == 8:
                        result.append(submat)
    return result 
