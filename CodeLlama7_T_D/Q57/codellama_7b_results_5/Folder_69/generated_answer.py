
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Iterate over each row in the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column in the matrix
        for j in range(matrix.shape[1]):
            # Create a copy of the original matrix
            submatrix = matrix.copy()

            # Remove the current row and column from the copy
            submatrix = np.delete(submatrix, i, axis=0)
            submatrix = np.delete(submatrix, j, axis=1)

            # Check if the sum of all integers in the submatrix is equal to 752
            if np.sum(submatrix) == 752:
                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices that have a sum of all integers equal to 752
    return submatrices
