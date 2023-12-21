
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count to 0
    count = 0
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # If the current element is equal to 121, increment the count
            if matrix[i][j] == 121:
                count += 1
    # Return the count of all submatrices with 121 integers each
    return count
