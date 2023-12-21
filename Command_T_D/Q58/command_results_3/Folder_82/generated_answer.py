import numpy as np
def submatrix_with_n_numbers(matrix):
    return sum(1 for r in range(len(matrix)) if np.all(matrix[r] == 99))
