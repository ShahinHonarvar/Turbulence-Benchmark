
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices_sum_equals_minus_779 = []
    rows, columns = np.shape(matrix)
    for row_size in range(1, rows+1):
        for col_size in range(1, columns+1):
            for r in range(rows - row_size + 1):
                for c in range(columns - col_size + 1):
                    submatrix = matrix[r: r+row_size, c: c+col_size]
                    if np.sum(submatrix) == -779:
                        submatrices_sum_equals_minus_779.append(submatrix)
    return submatrices_sum_equals_minus_779
