
import numpy as np
def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 15):
        for j in range(len(matrix[i]) - 15):
            submatrix = matrix[i:i+16, j:j+16]
            if np.sum(submatrix == 1) == 16:
                count += 1
    return count
