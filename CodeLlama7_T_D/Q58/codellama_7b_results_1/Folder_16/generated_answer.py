
import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 1):
        for j in range(cols - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if len(set(submatrix.flatten())) == 154:
                count += 1

    return count
