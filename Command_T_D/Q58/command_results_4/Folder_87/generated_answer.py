import numpy as np
def submatrix_with_n_numbers(matrix):
    return sum(1 for row in range(len(matrix)) if all(matrix[row][:96] == np.full(96, i, dtype=np.int) for i in range(len(matrix[row]))))
