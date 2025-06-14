
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Create a submatrix by selecting all elements in the current row and column
            submatrix = matrix[i:, j]
            # Check if the sum of all integers in the submatrix is equal to 41
            if np.sum(submatrix) == 41:
                # Add the submatrix to the result list
                result.append(submatrix)
    return result
