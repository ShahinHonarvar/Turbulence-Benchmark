
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Create a submatrix by selecting all rows and columns after (i, j)
            submatrix = matrix[i:, j:]
            # Check if the sum of all integers in the submatrix is equal to -3
            if np.sum(submatrix) == -3:
                # If it is, add it to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices
    return submatrices
