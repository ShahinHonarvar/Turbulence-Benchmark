
import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray, n: int) -> int:
    count = 0
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            submatrix = matrix[i:j]
            if len(submatrix) < n:
                continue

            if all(value == n for value in submatrix.flatten()):
                count += 1

    return count
