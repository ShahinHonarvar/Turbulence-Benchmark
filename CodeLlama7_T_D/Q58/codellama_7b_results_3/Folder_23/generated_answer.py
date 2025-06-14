
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 69 integers each
    count = 0

    # Loop through all rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # If the element at position (i, j) is equal to 69, increment the count
            if matrix[i][j] == 69:
                count += 1

    # Return the count of submatrices with 69 integers each
    return count
