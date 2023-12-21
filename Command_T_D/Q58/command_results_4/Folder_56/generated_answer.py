import numpy as np
def submatrix_with_n_numbers(matrix):
    return sum(np.all(matrix[i:j, i:j] == 68) for i in range(len(matrix)-67) for j in range(i+1, len(matrix)))
