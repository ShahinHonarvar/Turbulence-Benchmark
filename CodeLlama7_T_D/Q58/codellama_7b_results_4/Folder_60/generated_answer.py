
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0

    # Iterate over all rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # If the current element is equal to 88, increment the count
            if matrix[i, j] == 88:
                count += 1

    return count
