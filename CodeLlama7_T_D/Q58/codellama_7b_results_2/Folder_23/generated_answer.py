
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Get the current row of the matrix
        row = matrix[i]
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Get the current column of the matrix
            col = row[:, j]
            # Check if the submatrix contains 69 integers
            if np.count_nonzero(col == 69) == 69:
                # Increment the count variable
                count += 1

    # Return the count of all submatrices that contain 69 integers each
    return count
