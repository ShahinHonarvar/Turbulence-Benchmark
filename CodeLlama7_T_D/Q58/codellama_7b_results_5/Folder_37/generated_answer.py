
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices with 64 integers each
    count = 0

    # Iterate over all rows and columns in the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to the number of integers in a submatrix
            if matrix[i, j] == 64:
                # If it is, increment the counter by one
                count += 1

    # Return the count of all submatrices with 64 integers each
    return count
