
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the output list
    output = []
    # Loop through each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Find the submatrix with the desired sum
            if np.sum(matrix[i:, j]) == -47:
                output.append(matrix[i:, j])
    return output
