import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:j+166] == matrix[i:j+166], axis=1) for i in range(0, len(matrix)-165) for j in range(i, len(matrix)-165))
