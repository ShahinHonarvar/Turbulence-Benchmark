
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row, col = matrix.shape
    for i in range(row-6+1):
        for j in range(col-7+1):
            sub_matrix = matrix[i:i+6, j:j+7]
            if np.count_nonzero(sub_matrix == 49) == 49:
                count += 1
    return count
