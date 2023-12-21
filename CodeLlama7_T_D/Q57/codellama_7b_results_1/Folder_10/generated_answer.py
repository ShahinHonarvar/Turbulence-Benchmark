
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the output list
    output = []
    # Loop over all rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Calculate the sum of all integers in the submatrix starting from (i, j)
            sum = np.sum(matrix[i:, j:])
            # If the sum is equal to 56, add the submatrix to the output list
            if sum == 56:
                output.append(matrix[i:, j:])
    # Return the output list
    return output
