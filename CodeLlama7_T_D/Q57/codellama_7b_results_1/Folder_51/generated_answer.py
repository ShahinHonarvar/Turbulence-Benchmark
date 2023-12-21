
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Create a submatrix by selecting all elements except the current element
            submatrix = matrix[:i, :j] + matrix[i+1:, j+1:]
            # Check if the sum of the elements in the submatrix is equal to -46
            if np.sum(submatrix) == -46:
                # If the condition is true, add the submatrix to the result list
                result.append(submatrix)
    # Return the result list
    return result
