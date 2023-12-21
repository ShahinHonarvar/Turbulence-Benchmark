
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 87 integers each
    count = 0
    # Iterate over the rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 87
            if matrix[i, j] == 87:
                # Increment the count of submatrices with 87 integers each
                count += 1

    return count
