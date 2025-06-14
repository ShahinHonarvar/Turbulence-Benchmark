
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0

    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 96
            if matrix[i, j] == 96:
                # Increment the count variable
                count += 1

    # Return the count of all submatrices that contain 96 integers each
    return count
