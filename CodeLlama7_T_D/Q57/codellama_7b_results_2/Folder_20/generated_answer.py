
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Extract a submatrix from the current row and column
            submatrix = matrix[i:, j:]

            # Check if the sum of all integers in the submatrix equals -57
            if np.sum(submatrix) == -57:
                # If so, add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices that satisfy the condition
    return submatrices
