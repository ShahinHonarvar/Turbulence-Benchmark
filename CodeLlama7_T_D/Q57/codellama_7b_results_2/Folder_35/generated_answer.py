
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []
    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Calculate the sum of all integers in the submatrix
            submatrix_sum = np.sum(matrix[i:,j]) + np.sum(matrix[i,j+1:])
            # Check if the submatrix sum is equal to 432
            if submatrix_sum == 432:
                # Add the submatrix to the result list
                result.append(matrix[i:,j] + matrix[i,j+1:])
    # Return the result list
    return result
