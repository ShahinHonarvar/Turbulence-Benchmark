
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape[0], matrix.shape[1]
    result_submatrices = []
    for sub_rows in range(1, rows+1):
        for sub_cols in range(1, cols+1):
            for start_row in range(rows-sub_rows+1):
                for start_col in range(cols-sub_cols+1):
                    submatrix = matrix[start_row:(start_row+sub_rows), start_col:(start_col+sub_cols)]
                    if np.sum(submatrix) == -617:
                        result_submatrices.append(submatrix)
    return result_submatrices
