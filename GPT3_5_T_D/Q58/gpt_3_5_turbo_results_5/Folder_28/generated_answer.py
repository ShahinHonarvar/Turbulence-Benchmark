
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape

    for i in range(rows):
        for j in range(columns):
            if matrix[i, j] == 37:
                for row_length in range(i, rows):
                    for col_length in range(j, columns):
                        submatrix = matrix[i:row_length+1, j:col_length+1]
                        if np.sum(submatrix) == 37 * submatrix.size:
                            count += 1

    return count
