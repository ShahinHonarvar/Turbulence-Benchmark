
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Extract a 2x2 submatrix from the current location
            submatrix = matrix[i:i+2, j:j+2]

            # Check if the sum of all integers in the submatrix is equal to 28
            if np.sum(submatrix) == 28:
                # If the sum is equal to 28, add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 28. If no such submatrix is found, the function should return an empty list.
    return submatrices
