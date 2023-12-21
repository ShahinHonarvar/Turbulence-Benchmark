
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Extract the submatrix with a size of 3x3 from the current position (i, j)
            submatrix = matrix[i:i+3, j:j+3]
            # Check if the sum of all integers in the submatrix is equal to -97
            if np.sum(submatrix) == -97:
                # If the condition is met, add the submatrix to the list of submatrices
                submatrices.append(submatrix)
    # Return the list of all submatrices with a sum of -97
    return submatrices
