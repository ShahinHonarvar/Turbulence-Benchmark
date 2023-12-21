
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Check if the matrix is empty
    if matrix.size == 0:
        return []

    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Create a copy of the original matrix
        submatrix = np.copy(matrix)

        # Delete the first column and row from the submatrix
        submatrix = np.delete(submatrix, 0, axis=1)
        submatrix = np.delete(submatrix, i, axis=0)

        # Check if the sum of all integers in the submatrix is equal to 100
        if np.sum(submatrix) == 100:
            # Add the submatrix to the list of submatrices
            submatrices.append(submatrix)

    # Return the list of submatrices
    return submatrices
