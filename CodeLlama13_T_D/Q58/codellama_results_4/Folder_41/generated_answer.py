
import numpy as np
def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows-6):
        for j in range(num_cols-6):
            submatrix = matrix[i:i+7,j:j+7]
            if np.count_nonzero(submatrix == 73) == 49:
                count += 1
    return count
