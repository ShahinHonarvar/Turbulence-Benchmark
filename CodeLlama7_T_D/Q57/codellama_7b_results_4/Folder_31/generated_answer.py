
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Create a copy of the original matrix
            submatrix = matrix.copy()

            # Remove the current row and column from the submatrix
            del submatrix[i]
            del submatrix[:, j]

            # Check if the sum of all integers in the submatrix equals -44
            if np.sum(submatrix) == -44:
                # If it does, add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices that satisfy the condition
    return submatrices
