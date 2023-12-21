import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:j+186] == np.full(186, True), axis=1) for i in range(0, len(matrix)-185) for j in range(i+1, len(matrix)))
