
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the result
    result = []

    # Iterate over all possible starting rows and columns
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current submatrix has a sum equal to -25
            if np.sum(matrix[i:, j:]) == -25:
                # Add the current submatrix to the result list
                result.append(matrix[i:, j:].copy())

    return result
