
import numpy as np
def submatrix_with_n_numbers(matrix):
    # Initialize count variable
    count = 0
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Check if the element at (i,j) is equal to 138
            if matrix[i][j] == 138:
                # If it is, increment count by 1
                count += 1
    # Return count variable
    return count
