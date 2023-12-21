
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []

    # Loop over all possible starting indices of the submatrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix[0])):
            # Calculate the sum of the submatrix
            sum_submatrix = np.sum(matrix[i:j + 1])

            # Check if the sum is equal to 99
            if sum_submatrix == 99:
                # Add the submatrix to the result list
                result.append(matrix[i:j + 1])

    # Return the result list
    return result
