
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count to 0
    count = 0
    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # If the element at position (i, j) is equal to 180
            if matrix[i][j] == 180:
                # Increment the count by 1
                count += 1
    return count
