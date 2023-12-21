
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Extract a submatrix of size n by n from the current cell (i, j)
            submatrix = matrix[i:i+n, j:j+n]

            # Check if the submatrix contains 68 integers each
            if np.count_nonzero(submatrix == 68) == (n**2):
                # Increment the count variable if a matching submatrix is found
                count += 1

    # Return the count of all submatrices that contain 68 integers each
    return count
