import numpy as np
def submatrix_with_n_numbers(matrix):
    m, n = len(matrix), len(matrix[0])
    return np.sum(1 for i in range(m) for j in range(n) if matrix[i][j] == 99 and matrix[i][j+1] == 99 and matrix[i+1][j] == 99 and matrix[i+1][j+1] == 99)
