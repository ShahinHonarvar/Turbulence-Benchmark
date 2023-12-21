
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the output list
    output = []
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Create a submatrix with the current row and column as its upper-left corner
            submatrix = matrix[i:, j:]
            # Check if the sum of all integers in the submatrix is equal to 95
            if np.sum(submatrix) == 95:
                # If so, append the submatrix to the output list
                output.append(submatrix)
    # Return the output list
    return output
