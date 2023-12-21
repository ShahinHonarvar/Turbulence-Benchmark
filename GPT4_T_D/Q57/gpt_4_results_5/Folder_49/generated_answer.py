
import numpy as np

def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    result = []
    rows, cols = matrix.shape

    for row_size in range(1, rows+1):
        for col_size in range(1, cols+1):
            for start_row in range(0, rows-row_size+1):
                for start_col in range(0, cols-col_size+1):
                    sub_matrix = matrix[start_row:start_row+row_size,start_col:start_col+col_size]
                    if sub_matrix.sum() == -42:
                        result.append(sub_matrix.tolist())
    return result
