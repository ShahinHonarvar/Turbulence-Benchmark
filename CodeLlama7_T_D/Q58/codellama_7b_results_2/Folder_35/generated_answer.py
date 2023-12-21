
import numpy as np
def submatrix_with_n_numbers(matrix):
    # Initialize a count variable to keep track of the number of submatrices with 111 integers each
    count = 0
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 111
            if matrix[i][j] == 111:
                # If it is, increment the count variable by 1
                count += 1
    # Return the count variable as the final answer
    return count
