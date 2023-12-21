
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape

    for row_num in range(rows):
        for col_num in range(columns):
            for row_limit in range(row_num+1, rows+1):
                for col_limit in range(col_num+1, columns+1):
                    submatrix = matrix[row_num:row_limit, col_num:col_limit]
                    if np.size(submatrix) == 77:
                        count += 1

    return count
