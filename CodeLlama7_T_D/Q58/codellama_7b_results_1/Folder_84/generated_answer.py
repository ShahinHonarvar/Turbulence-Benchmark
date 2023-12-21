
import numpy as np
def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 127 integers each to 0
    count = 0
    # Iterate over the rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 127
            if matrix[i,j] == 127:
                # If it is, increment the count of submatrices with 127 integers each
                count += 1
    return count
