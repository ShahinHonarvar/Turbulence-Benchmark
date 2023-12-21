
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []

    # Loop through each submatrix of the given matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the sum of all integers in the current submatrix equals 862
            if np.sum(matrix[i:, j:]) == 862:
                # If so, add the submatrix to the results list
                result.append(matrix[i:, j:].copy())

    # Return the results list
    return result
