
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []
    # Loop over each submatrix in the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Calculate the sum of all integers in the current submatrix
            submatrix_sum = np.sum(matrix[i:i+2, j:j+2])
            # If the sum is equal to 87, add the submatrix to the result list
            if submatrix_sum == 87:
                result.append(matrix[i:i+2, j:j+2])
    return result
