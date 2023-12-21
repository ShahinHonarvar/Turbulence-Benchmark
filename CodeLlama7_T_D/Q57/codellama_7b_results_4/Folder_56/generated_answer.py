
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Extract a submatrix of size (2, 2) starting at position (i, j)
            submatrix = matrix[i:i+2, j:j+2]

            # Check if the sum of all integers in the submatrix is equal to -50
            if np.sum(submatrix) == -50:
                # If it is, add it to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices
    return submatrices
