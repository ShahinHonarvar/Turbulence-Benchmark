
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []
    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the sum of all integers in the submatrix equals 19
            if np.sum(matrix[i:, j]) == 19:
                # Add the submatrix to the result list
                result.append(matrix[i:, j])
    # Return the result list
    return result
