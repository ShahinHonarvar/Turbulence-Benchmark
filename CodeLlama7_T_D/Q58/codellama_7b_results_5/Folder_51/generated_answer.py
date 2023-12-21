
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 95 integers each to 0
    count = 0
    # Loop through all rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current submatrix contains 95 integers each
            if np.count_nonzero(matrix[i:i+95, j:j+95]) == 95 * 95:
                # Increment the count of submatrices with 95 integers each
                count += 1
    # Return the count of all submatrices of the given matrix that contain 95 integers each
    return count
