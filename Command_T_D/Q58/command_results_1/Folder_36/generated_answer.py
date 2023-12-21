import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    return sum(~np.all(np.sum(matrix[i:j], axis=1) == np.full(j-i, 131, np.int8)) for i in range(len(matrix)-130) for j in range(i+130, len(matrix)))
