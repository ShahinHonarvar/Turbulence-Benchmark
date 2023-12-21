
import numpy as np
def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 159 integers each to 0
    count = 0
    # Loop over the rows and columns of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Check if the current submatrix has 159 integers each
            if sum(matrix[i][j]) == 159:
                # Increment the count of submatrices with 159 integers each
                count += 1

    return count
