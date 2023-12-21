
import numpy as np

def submatrix_with_particular_sum(matrix, sum):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Extract a submatrix from the current row and column
            submatrix = matrix[i:, j:]
            # Check if the sum of all integers in the submatrix is equal to the given sum
            if np.sum(submatrix) == sum:
                # If the sum is equal to the given sum, add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices that have a sum equal to the given sum
    return submatrices
