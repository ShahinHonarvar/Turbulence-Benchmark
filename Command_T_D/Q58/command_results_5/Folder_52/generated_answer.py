import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(np.equal(matrix[i:j+1], 147), axis=1) for i in range(len(matrix)-146) for j in range(i+1, len(matrix)))
