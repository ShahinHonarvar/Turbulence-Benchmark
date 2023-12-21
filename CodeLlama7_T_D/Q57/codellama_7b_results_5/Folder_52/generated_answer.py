
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a submatrix with the same dimensions as the original matrix
            submatrix = np.zeros((matrix.shape[0], matrix.shape[1]))

            # Set the current element of the submatrix to 1
            submatrix[i, j] = 1

            # Check if the sum of all integers in the submatrix is equal to 100
            if np.sum(submatrix) == 100:
                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 100, or an empty list if no such submatrix is found.
    return submatrices
