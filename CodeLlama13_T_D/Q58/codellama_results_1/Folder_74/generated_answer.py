
import numpy as np

def submatrix_with_n_numbers(matrix):
    return len([i for i in range(len(matrix)) if np.count_nonzero(np.array(matrix[i])) == 48])
