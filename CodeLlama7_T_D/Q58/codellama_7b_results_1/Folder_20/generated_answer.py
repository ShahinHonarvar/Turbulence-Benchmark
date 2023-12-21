
import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    count = 0
    for i in range(matrix.shape[0] - 3):
        for j in range(matrix.shape[1] - 3):
            submatrix = matrix[i : i + 4, j : j + 4]
            if np.all(submatrix == 49):
                count += 1
    return count
