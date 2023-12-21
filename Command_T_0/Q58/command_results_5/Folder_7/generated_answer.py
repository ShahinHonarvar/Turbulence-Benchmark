import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:j+121] == matrix[i:j+121], axis=1) for i in range(0, len(matrix)-120) for j in range(i, len(matrix)-1))
