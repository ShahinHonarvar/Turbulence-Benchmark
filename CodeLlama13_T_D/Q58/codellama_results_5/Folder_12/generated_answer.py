
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 3):
        for j in range(len(matrix[0]) - 3):
            submat = matrix[i:i+4, j:j+4]
            if np.allclose(submat, 46):
                count += 1
    return count
