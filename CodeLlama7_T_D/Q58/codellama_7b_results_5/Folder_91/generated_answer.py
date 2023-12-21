
import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    # Initialize the count of submatrices with 5 integers each
    count = 0

    # Iterate over the rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current element is part of a submatrix with 5 integers each
            if matrix[i][j] != 0 and np.sum(matrix[i][j]:matrix[i][j]+5) == 5:
                # Increment the count of submatrices with 5 integers each
                count += 1

    # Return the count of submatrices with 5 integers each
    return count
