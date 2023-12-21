
import numpy as np
def submatrix_with_n_numbers(matrix):
    # Initialize the count to 0
    count = 0
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 147
            if matrix[i,j] == 147:
                # Increment the count by 1
                count += 1
    # Return the count of submatrices with 147 integers each
    return count
