import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.count_nonzero(np.any(matrix[i:i+20] for i in range(0,len(matrix)-19),1)))
