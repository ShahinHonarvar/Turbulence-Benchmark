
import numpy as np
def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 2):
        for j in range(i + 1, len(matrix) - 1):
            submatrix = matrix[i:j+1]
            if np.count_nonzero(submatrix == 39) == (j - i + 1) * 39:
                count += 1
    return count
