import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.matrix(matrix)
    return sum(sum(matrix[i][:47]) == 47 for i in range(len(matrix)))
