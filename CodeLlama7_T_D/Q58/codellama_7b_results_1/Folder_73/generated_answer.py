
import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray, n: int) -> int:
    count = 0
    for i in range(matrix.shape[0] - n + 1):
        for j in range(matrix.shape[1] - n + 1):
            if all(x == n for x in matrix[i:i+n, j:j+n].ravel()):
                count += 1

    return count
