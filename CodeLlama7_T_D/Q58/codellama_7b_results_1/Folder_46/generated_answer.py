
import numpy as np
def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 144 integers each
    count = 0
    # Loop over all rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 144
            if matrix[i,j] == 144:
                # If it is, increment the count of submatrices with 144 integers each
                count += 1
    # Return the count of submatrices with 144 integers each
    return count
