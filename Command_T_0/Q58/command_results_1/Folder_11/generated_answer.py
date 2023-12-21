import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:j+38] == matrix[i:j+38], axis=1) for i in range(len(matrix)-37) for j in range(i+1, len(matrix)-1))
