
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0

    # Loop over all rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # If the current element is a 120, increment the count
            if matrix[i][j] == 120:
                count += 1

    # Return the count of submatrices with 120 integers each
    return count
