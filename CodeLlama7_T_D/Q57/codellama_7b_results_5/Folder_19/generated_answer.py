
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the output list
    output = []
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Calculate the sum of all integers in the submatrix
            submatrix_sum = np.sum(matrix[i:, j]) + np.sum(matrix[i, j+1:]) - matrix[i, j]
            # Check if the sum is equal to -97
            if submatrix_sum == -97:
                # Add the submatrix to the output list
                output.append(matrix[i:, j][0])
    # Return the output list
    return output
