
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
            submatrix = np.delete(submatrix, i, 0)
            submatrix = np.delete(submatrix, j, 1)

            # Check if the sum of all integers in the submatrix is equal to -394
            if np.sum(submatrix) == -394:
                # If it is, add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of all submatrices that have a sum of -394
    return submatrices
