
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count to 0
    count = 0
    # Loop through each row of the matrix
    for i in range(matrix.shape[0] - 1):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1] - 1):
            # Check if the current submatrix contains 186 integers
            if (matrix[i:i+2, j:j+2] == 186).all():
                # If it does, increment the count
                count += 1

    # Return the count of all submatrices that contain 186 integers each
    return count
