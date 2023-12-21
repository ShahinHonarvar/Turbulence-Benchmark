
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Extract a submatrix from the current cell (i, j)
            submatrix = matrix[i:i+1, j:j+1]

            # Check if the sum of all integers in the submatrix equals -157
            if np.sum(submatrix) == -157:
                # If yes, add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices that satisfy the condition
    return submatrices
