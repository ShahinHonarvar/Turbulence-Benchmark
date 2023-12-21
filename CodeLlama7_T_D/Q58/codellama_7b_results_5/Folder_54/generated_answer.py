
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count to 0
    count = 0
    # Iterate over all rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 27
            if matrix[i][j] == 27:
                # If it is, increment the count by 1
                count += 1

    # Return the count of all submatrices that contain 27 integers each
    return count
