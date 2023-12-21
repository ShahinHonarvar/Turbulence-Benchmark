
import numpy as np

def submatrix_with_particular_sum(matrix, sum):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Create a copy of the original matrix
            submatrix = matrix.copy()
            # Remove all elements from the row and column i
            submatrix = np.delete(submatrix, i, 0)
            submatrix = np.delete(submatrix, j, 1)
            # Check if the sum of all elements in the submatrix is equal to the target sum
            if np.sum(submatrix) == sum:
                # If so, add the submatrix to the list of submatrices
                submatrices.append(submatrix)
    return submatrices
