
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Extract the submatrix with the given indices
            submatrix = matrix[i:i+1, j:j+1]

            # Check if the sum of all integers in the submatrix is equal to 27
            if np.sum(submatrix) == 27:
                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices
    return submatrices
