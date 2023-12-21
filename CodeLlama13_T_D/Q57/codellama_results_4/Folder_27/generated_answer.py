
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            curr_row, curr_col = i, j
            while curr_row < rows and curr_col < cols:
                submatrix = matrix[curr_row:curr_row+1, curr_col:curr_col+1]
                if np.sum(submatrix) == 77:
                    return [submatrix]
                else:
                    curr_row += 1
                    curr_col += 1
    return []
