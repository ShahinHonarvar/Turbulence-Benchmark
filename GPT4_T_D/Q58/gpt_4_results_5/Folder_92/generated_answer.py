
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row, col = np.shape(matrix)
    for i in range(row):
        for j in range(col):
            for sub_row in range(i, row):
                for sub_col in range(j, col):
                    sub_matrix = matrix[i:sub_row+1, j:sub_col+1]
                    if sub_matrix.size == 8:
                        count += 1
    return count
