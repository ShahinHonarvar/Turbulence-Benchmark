
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 16 integers each to 0
    count = 0
    # Loop over all rows and columns in the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current element is 16, and if so, increment the count of submatrices with 16 integers each
            if matrix[i][j] == 16:
                count += 1
    return count
