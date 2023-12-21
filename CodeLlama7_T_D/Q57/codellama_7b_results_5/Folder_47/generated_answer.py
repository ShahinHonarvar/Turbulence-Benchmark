
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Extract a submatrix from the original matrix with size 2x2, starting at (i,j)
            submatrix = matrix[i:i+2, j:j+2]
            # Check if the sum of all integers in the submatrix is equal to 27
            if np.sum(submatrix) == 27:
                # If it is, add it to the result list
                result.append(submatrix)
    # Return the result list
    return result
