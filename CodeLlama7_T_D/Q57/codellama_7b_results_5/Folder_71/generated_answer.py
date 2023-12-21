
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []
    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Create a submatrix with the current row and column
            submatrix = np.copy(matrix)
            submatrix = submatrix[i:i+1, j:j+1]
            # Check if the sum of all integers in the submatrix is equal to 69
            if np.sum(submatrix) == 69:
                # If it is, add it to the result list
                result.append(submatrix)
    return result
