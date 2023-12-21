
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0

    # Loop through each row of the matrix
    for i in range(matrix.shape[0] - 1):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1] - 1):
            # Check if the submatrix has 176 integers
            if np.count_nonzero(matrix[i:i + 2, j:j + 2]) == 176:
                # Increment the count variable
                count += 1

    # Return the count of all submatrices that contain 176 integers each
    return count
