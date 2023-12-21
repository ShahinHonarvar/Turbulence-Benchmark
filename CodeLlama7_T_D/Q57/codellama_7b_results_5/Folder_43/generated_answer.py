
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Create a copy of the original matrix
            submatrix = matrix.copy()
            # Remove the rows and columns from the original matrix that are not part of the current submatrix
            submatrix = submatrix[i:, j:]
            # Check if the sum of all integers in the current submatrix is equal to -81
            if np.sum(submatrix) == -81:
                # If the sum is equal to -81, add the current submatrix to the list of submatrices
                submatrices.append(submatrix)
    # Return the list of all submatrices that have a sum of all integers equal to -81
    return submatrices
