
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Create a submatrix of size 2x2 starting at the current position
            submatrix = matrix[i:i+2, j:j+2]
            # Check if the sum of all integers in the submatrix equals 616
            if np.sum(submatrix) == 616:
                # If yes, add the submatrix to the result list
                result.append(submatrix)
    # Return the result list
    return result
