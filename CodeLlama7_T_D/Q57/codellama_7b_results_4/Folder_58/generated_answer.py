
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []

    # Loop through each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Find the sum of all integers in the submatrix
            submatrix_sum = np.sum(matrix[i:, j]) + np.sum(matrix[i, j+1:])
            # If the sum is equal to -137, add the submatrix to the result list
            if submatrix_sum == -137:
                result.append(matrix[i:, j] * matrix[i, j+1:] > 0))
    return result
