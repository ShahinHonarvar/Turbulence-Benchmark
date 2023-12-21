
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize the count to 0
    count = 0
    # Loop over each row and column in the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current submatrix contains n integers
            if np.sum(matrix[i:, j]) == n:
                # Increment the count by 1
                count += 1
    # Return the count of all submatrices that contain n integers each
    return count
