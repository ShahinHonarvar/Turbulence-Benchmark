
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []

    # Iterate over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Find the sum of all integers in the submatrix
            submatrix_sum = np.sum(matrix[i:, j]) + np.sum(matrix[i, j+1:])
            # If the sum is equal to -617, add the submatrix to the result list
            if submatrix_sum == -617:
                result.append(matrix[i:, j])
                result.append(matrix[i, j+1:])
    return result
