
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []

    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Calculate the sum of all integers in the submatrix starting from (i, j) and having size (3, 3)
            submatrix_sum = np.sum(matrix[i:i+3, j:j+3])

            # If the sum is equal to -308, add the submatrix to the result list
            if submatrix_sum == -308:
                result.append(matrix[i:i+3, j:j+3])

    # Return the result list
    return result
