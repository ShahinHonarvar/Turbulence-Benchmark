
import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = np.shape(matrix)
    count = 0
    for sub_row in range(row):
        for sub_col in range(col):
            for super_row in range(sub_row+1, row+1):
                for super_col in range(sub_col+1, col+1):
                    submatrix = matrix[sub_row:super_row, sub_col:super_col]
                    if np.size(submatrix) == 131:
                        count += 1
    return count
