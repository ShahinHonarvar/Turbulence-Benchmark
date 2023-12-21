
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []
    # Loop over all rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Get the submatrix by slicing the original matrix
            submatrix = matrix[i:i+1, j:j+1]
            # Check if the sum of all integers in the submatrix is equal to 830
            if np.sum(submatrix) == 830:
                # Add the submatrix to the result list
                result.append(submatrix)
    # Return the result list
    return result
