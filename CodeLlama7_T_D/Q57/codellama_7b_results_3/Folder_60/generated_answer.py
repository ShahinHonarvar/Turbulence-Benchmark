
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []
    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Calculate the sum of all elements in the submatrix
            submatrix_sum = np.sum(matrix[i:, j:])
            # If the sum is equal to 94, add the submatrix to the result list
            if submatrix_sum == 94:
                result.append(matrix[i:, j:])
    # Return the result list
    return result
