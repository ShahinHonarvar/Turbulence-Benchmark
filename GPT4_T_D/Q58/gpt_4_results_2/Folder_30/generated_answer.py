
import numpy as np

def submatrix_with_n_numbers(matrix):
    total_count = 0
    rows, cols = matrix.shape
    len_matrix = np.prod(matrix.shape)
    if len_matrix < 94:
        return 0
    for submatrix_size in range(1, int(np.sqrt(94)) + 1):
        if 94 % submatrix_size == 0:
            other_dimension_size = 94 // submatrix_size
            for i in range(rows - submatrix_size + 1):
                for j in range(cols - other_dimension_size + 1):
                    total_count += 1
    return total_count
