
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 1):
        for j in range(i + 1, len(matrix)):
            submatrix = matrix[i:j]
            if np.count_nonzero(submatrix == 69) == (j - i) * 69:
                count += 1

    return count
