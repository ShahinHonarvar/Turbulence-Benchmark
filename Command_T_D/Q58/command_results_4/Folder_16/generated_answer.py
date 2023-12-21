import numpy as np
def submatrix_with_n_numbers(matrix):
    return sum(1 for i in range(matrix.shape[0] - 153) for j in range(matrix.shape[1] - 153) for submatrix in np.nditer(matrix[i:i + 154][j:j + 154]))
