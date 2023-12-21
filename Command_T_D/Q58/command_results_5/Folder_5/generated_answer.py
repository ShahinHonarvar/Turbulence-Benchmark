import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(
        np.any(np.array([np.all(matrix[i][:63] == matrix[i][63:]) for i in range(len(matrix))]), axis=0),
        dtype=np.int32,
    )
