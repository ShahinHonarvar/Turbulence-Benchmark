
import numpy as np

def submatrix_with_particular_sum(matrix):
    results = []
    rows, cols = np.shape(matrix)
    for row_start in range(rows):
        for col_start in range(cols):
            for row_end in range(row_start+1, rows+1):
                for col_end in range(col_start+1, cols+1):
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    if np.sum(submatrix) == -83:
                        results.append(submatrix)
    return results
