
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for sub_rows in range(1, rows+1):
        for sub_cols in range(1, cols+1):
            for r in range(0, rows - sub_rows + 1):
                for c in range(0, cols - sub_cols + 1):
                    if np.size(matrix[r:r+sub_rows, c:c+sub_cols]) == 111:
                        count += 1
    return count
