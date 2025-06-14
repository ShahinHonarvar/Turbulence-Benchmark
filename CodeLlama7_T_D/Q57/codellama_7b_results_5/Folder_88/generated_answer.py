
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Extract a 2x2 submatrix from the current position (i, j)
            submatrix = matrix[i:i+2, j:j+2]
            # Check if the sum of all integers in the submatrix equals -64
            if np.sum(submatrix) == -64:
                # If yes, add the submatrix to the list of submatrices
                submatrices.append(submatrix)
    # Return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -64. If no such submatrix is found, the function should return an empty list.
    return submatrices
