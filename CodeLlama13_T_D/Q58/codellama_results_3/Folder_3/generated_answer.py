
import numpy as np
def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m-4):
        for j in range(n-4):
            submatrix = matrix[i:i+5,j:j+5]
            if np.all(submatrix == 54):
                count += 1
    return count
