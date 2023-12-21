
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Extract a submatrix from the original matrix
            submatrix = matrix[i:, j:]
            # Check if the sum of all integers in the submatrix is equal to -57
            if np.sum(submatrix) == -57:
                # If the condition is met, append the submatrix to the list of submatrices
                submatrices.append(submatrix)
    # Return the list of submatrices that satisfy the condition
    return submatrices
