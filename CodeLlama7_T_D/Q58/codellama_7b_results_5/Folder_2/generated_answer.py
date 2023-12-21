
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count to 0
    count = 0
    # Iterate over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 107
            if matrix[i, j] == 107:
                # If it is, increment the count by 1
                count += 1
    # Return the count of all submatrices that contain 107 integers each
    return count
