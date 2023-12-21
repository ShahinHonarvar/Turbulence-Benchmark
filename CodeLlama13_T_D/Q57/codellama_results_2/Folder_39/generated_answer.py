
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []

    # Iterate over all possible rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the sum of the submatrix starting from (i, j) is equal to 66
            if np.sum(matrix[i:, j:]) == 66:
                # If so, add the submatrix to the result list
                result.append(matrix[i:, j:])

    # Return the result list
    return result
