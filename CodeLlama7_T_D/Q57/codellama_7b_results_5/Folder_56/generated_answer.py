
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the output list
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Get the submatrix of the current row and column
            submatrix = matrix[i:, j:]

            # Check if the sum of all integers in the submatrix is equal to -50
            if np.sum(submatrix) == -50:
                # If it is, add the submatrix to the output list
                submatrices.append(submatrix)

    # Return the output list of submatrices
    return submatrices
