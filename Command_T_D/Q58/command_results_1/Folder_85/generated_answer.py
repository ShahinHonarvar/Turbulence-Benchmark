import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:i+13] == range(1,14), axis=1) for i in range(0,len(matrix)-12))
