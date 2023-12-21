
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for sub_rows in range(1, rows+1):
        for sub_cols in range(1, cols+1):
            submatrices = [matrix[i:i+sub_rows, j:j+sub_cols] for i in range(rows-sub_rows+1) for j in range(cols-sub_cols+1) if np.size(matrix[i:i+sub_rows, j:j+sub_cols], axis=(0,1)) == 179]
            count += len(submatrices)
    return count
