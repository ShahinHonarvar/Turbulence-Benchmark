
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for sub_rows in range(1, rows+1):
        for sub_cols in range(1, cols+1):
            for i in range(0, rows-sub_rows+1):
                for j in range(0, cols-sub_cols+1):
                    sub_matrix = matrix[i:i+sub_rows, j:j+sub_cols]
                    if np.size(sub_matrix) == 67:
                        count += 1
    return count
