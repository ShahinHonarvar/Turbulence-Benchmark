
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            submatrix = matrix[i:i+2, j:j+2]
            if np.count_nonzero(submatrix == 45) == 45:
                count += 1

    return count
