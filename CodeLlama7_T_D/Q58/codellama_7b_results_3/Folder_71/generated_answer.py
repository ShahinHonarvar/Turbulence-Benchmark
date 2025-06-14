
import numpy as np
def submatrix_with_n_numbers(matrix):
    # Initialize count to 0
    count = 0
    # Loop over all rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # If the current element is equal to 78, increment the count
            if matrix[i][j] == 78:
                count += 1

    # Return the count of all submatrices that contain 78 integers each
    return count
