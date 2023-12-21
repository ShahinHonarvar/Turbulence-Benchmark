
import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray, n: int) -> int:
    # Initialize the count of submatrices with 107 integers each
    count = 0

    # Loop over all rows and columns in the matrix
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            # Check if the current element is equal to 107
            if matrix[row, col] == 107:
                # Increment the count of submatrices with 107 integers each
                count += 1

    return count
