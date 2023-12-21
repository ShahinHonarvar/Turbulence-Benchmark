
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []

    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Calculate the sum of all integers in the submatrix starting from (i,j)
            current_sum = np.sum(matrix[i:, j:])

            # If the sum is 40, add the submatrix to the result list
            if current_sum == 40:
                result.append((i, j))

    return result
