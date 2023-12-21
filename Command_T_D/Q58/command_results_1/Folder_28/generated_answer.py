import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:j+1] == np.full(37, -1), axis=1) for i in range(len(matrix)-36) for j in range(i+1, len(matrix)-1))
