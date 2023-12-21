import numpy as np
def submatrix_with_n_numbers(matrix):
    return sum(1 for row in range(len(matrix)) if np.array(list(matrix[row])).shape[0] == 9)
