
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for i in range(row+1, rows+1):
                for j in range(col+1, cols+1):
                    sub_matrix = matrix[row:i, col:j]
                    if np.sum(sub_matrix) == 432:
                        return sub_matrix.tolist()
    return []
