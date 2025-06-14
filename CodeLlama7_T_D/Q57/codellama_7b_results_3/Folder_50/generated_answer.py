
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Get the row of the current iteration
        row = matrix[i]
        # Check if the sum of all elements in the row is equal to 95
        if np.sum(row) == 95:
            # If so, add the row to the result list
            result.append(row)
    # Return the result list
    return result
