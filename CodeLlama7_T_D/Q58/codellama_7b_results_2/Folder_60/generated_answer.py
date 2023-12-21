
import numpy as np
def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 87):
        for j in range(matrix.shape[1] - 87):
            if matrix[i:i+88, j:j+88].all():
                count += 1

    return count
