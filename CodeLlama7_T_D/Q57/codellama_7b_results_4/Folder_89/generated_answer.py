
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the output list
    output = []
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Extract the submatrix of size 2x2 starting at (i, j)
            submatrix = matrix[i:i+2, j:j+2]
            # Check if the sum of all integers in the submatrix is equal to 80
            if np.sum(submatrix) == 80:
                # If it is, add the submatrix to the output list
                output.append(submatrix)
    # Return the output list
    return output
