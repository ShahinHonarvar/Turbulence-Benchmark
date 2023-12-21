
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0

    # Iterate over each row and column of the matrix
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Get the current submatrix
            submatrix = matrix[i:i + 2, j:j + 2]

            # Check if the submatrix contains 24 integers
            if np.count_nonzero(submatrix) == 24:
                count += 1

    # Return the count of all submatrices that contain 24 integers each
    return count
