
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 59):
        for j in range(matrix.shape[1] - 59):
            if (matrix[i:i+60, j:j+60] == np.ones((60, 60)) * 60).all():
                count += 1

    return count
