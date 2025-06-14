
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 74 + 1):
        for j in range(matrix.shape[1] - 74 + 1):
            if np.all(matrix[i:i+74, j:j+74] == 74)):
                count += 1
    return count
