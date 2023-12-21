
import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray, n: int) -> int:
    """Return the count of all submatrices of matrix that contain n integers each."""
    if matrix.size == 0 or n <= 0:
        return 0

    count = 0

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            submatrix = matrix[i:, j:]
            if submatrix.size == n:
                count += 1

    return count
