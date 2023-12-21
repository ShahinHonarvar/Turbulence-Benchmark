
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0

    # Loop over all rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 176
            if matrix[i, j] == 176:
                # If it is, increment the count variable
                count += 1

    # Return the count of all submatrices that contain 176 integers each
    return count
