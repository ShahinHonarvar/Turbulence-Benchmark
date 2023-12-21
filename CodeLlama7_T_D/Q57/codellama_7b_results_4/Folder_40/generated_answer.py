
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []
    # Loop over each row in the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column in the matrix
        for j in range(matrix.shape[1]):
            # Initialize a new submatrix with a single element
            submatrix = np.array([[matrix[i,j]]])
            # Check if the sum of all integers in the submatrix is equal to -10
            if np.sum(submatrix) == -10:
                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix)
    # Return the list of submatrices
    return submatrices
