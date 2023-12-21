
import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray, n: int) -> int:
    count = 0
    for i in range(matrix.shape[0] - n + 1):
        for j in range(matrix.shape[1] - n + 1):
            if all(matrix[i+k][j+l] == 72 for k in range(n) for l in range(n))):
                count += 1

    return count
