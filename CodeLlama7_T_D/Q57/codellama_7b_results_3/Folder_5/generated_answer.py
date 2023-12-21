
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []
    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Calculate the sum of all integers in the submatrix
            submatrix_sum = np.sum(matrix[i:,j]) + np.sum(matrix[i,j+1:]) - matrix[i,j]
            # If the sum is equal to -43, add the submatrix to the result list
            if submatrix_sum == -43:
                result.append(matrix[i:,j])
    return result
