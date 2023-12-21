
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    num_rows, num_cols = matrix.shape
    for i in range(num_rows - 1):
        for j in range(num_cols - 1):
            if np.count_nonzero(matrix[i:i+2, j:j+2] == 51) == 4:
                count += 1
    return count
