
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Extract the submatrix from the current position
            submatrix = matrix[i:, j:]

            # Check if the sum of all integers in the submatrix is equal to -936
            if np.sum(submatrix) == -936:
                # If it is, add it to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices that have a sum of all integers equal to -936
    return submatrices
