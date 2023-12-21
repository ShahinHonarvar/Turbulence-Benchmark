
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop through each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Get the current submatrix
            submatrix = matrix[i:, j:]

            # Check if the sum of all integers in the submatrix equals -27
            if np.sum(submatrix) == -27:
                # If so, add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -27
    return submatrices
