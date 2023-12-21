
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Create a copy of the original matrix
            submatrix = matrix.copy()
            # Remove the current row and column from the submatrix
            submatrix = np.delete(submatrix, i, 0)
            submatrix = np.delete(submatrix, j, 1)
            # Check if the sum of all integers in the submatrix is -811
            if submatrix.sum() == -811:
                # Add the submatrix to the result list
                result.append(submatrix)
    return result
