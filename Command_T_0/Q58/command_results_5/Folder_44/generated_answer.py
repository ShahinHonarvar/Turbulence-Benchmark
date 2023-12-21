import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:j+1] == 191, axis=1) for i in range(0, len(matrix)-190) for j in range(i+1, len(matrix)))
