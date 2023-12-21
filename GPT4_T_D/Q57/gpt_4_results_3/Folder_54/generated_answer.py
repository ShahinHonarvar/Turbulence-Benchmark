
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for row_size in range(1, rows+1):
        for col_size in range(1, cols+1):
            for r in range(0, rows-row_size+1):
                for c in range(0, cols-col_size+1):
                    submatrix = matrix[r:row_size+r, c:col_size+c]
                    if np.sum(submatrix) == -59:
                        result.append(submatrix)
    return result
