
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    m, n = len(matrix), len(matrix[0])
    for row_start in range(m):
        for col_start in range(n):
            for row_end in range(row_start, m):
                for col_end in range(col_start, n):
                    submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                    if np.sum(submatrix) == 411:
                        result.append(submatrix)
    return result
