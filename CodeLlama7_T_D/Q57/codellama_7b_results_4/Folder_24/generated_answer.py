
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop over each row and column in the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Create a copy of the original matrix
            submatrix = matrix.copy()

            # Remove the elements from the specified row and column
            for k in range(submatrix.shape[0] - 1, i, -1):
                for l in range(submatrix.shape[1] - 1, j, -1):
                    submatrix[k][l] = 0

            # Check if the sum of all integers in the submatrix is equal to -36
            if np.sum(submatrix) == -36:
                # If it is, add it to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices
    return submatrices
