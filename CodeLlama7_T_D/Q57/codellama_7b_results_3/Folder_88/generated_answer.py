
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices with the empty list
    submatrices = []
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Extract the submatrix with the current row and column
            submatrix = matrix[i:, j]
            # Check if the sum of all integers in the submatrix is equal to -64
            if np.sum(submatrix) == -64:
                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix)
    # Return the list of submatrices with the sum of all integers equal to -64, or an empty list if no such submatrix is found
    return submatrices
