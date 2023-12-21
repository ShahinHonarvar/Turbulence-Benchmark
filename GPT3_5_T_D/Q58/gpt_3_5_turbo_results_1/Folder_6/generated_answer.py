
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape

    for i in range(rows - 1):
        for j in range(columns - 1):
            submatrix = matrix[i:i+2, j:j+2]
            if np.count_nonzero(submatrix == 122) == 4:
                count += 1

    return count
