
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Create a copy of the original matrix
            submatrix = matrix.copy()
            # Remove the current row and column from the submatrix
            del submatrix[i, :]
            del submatrix[:, j]
            # Check if the sum of all integers in the submatrix is equal to -26
            if np.sum(submatrix) == -26:
                # If it is, add the submatrix to the list of submatrices
                submatrices.append(submatrix)
    # Return the list of submatrices that meet the condition
    return submatrices
