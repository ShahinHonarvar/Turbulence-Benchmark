
import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray, n: int) -> int:
    count = 0
    for i in range(matrix.shape[0] - n + 1):
        for j in range(matrix.shape[1] - n + 1):
            if all(x == y for x, y in zip(matrix[i:i+n, j:j+n].flatten(), [122] * n))):
                count += 1

    return count
