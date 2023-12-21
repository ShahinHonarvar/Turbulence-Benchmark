
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 7):
        for j in range(len(matrix[i]) - 7):
            submatrix = matrix[i:i+8, j:j+8]
            if np.count_nonzero(submatrix == 84) == 64:
                count += 1
    return count
