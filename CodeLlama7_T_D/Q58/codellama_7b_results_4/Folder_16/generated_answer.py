
import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    # Initialize the count of submatrices with 154 integers each
    count = 0

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] == 154:
                # Check if the submatrix with the current position of the number as its top-left corner has a count of 154 integers each
                temp_matrix = matrix[i:i + matrix.shape[0], j:j + matrix.shape[1]]
                if np.count_nonzero(temp_matrix) == 154:
                    # Increment the count of submatrices with 154 integers each
                    count += 1

    return count
