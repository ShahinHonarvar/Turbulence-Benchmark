
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []
    # Loop through each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Create a submatrix by selecting only the elements at the current row and column
            submatrix = matrix[i:i+1, j:j+1]
            # Check if the sum of all integers in the submatrix is equal to 66
            if np.sum(submatrix) == 66:
                # If it is, append the submatrix to the result list
                result.append(submatrix)
    # Return the result list
    return result
