
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Create a copy of the original matrix
            submatrix = matrix.copy()
            # Remove all elements from the submatrix that are not in the current row or column
            submatrix = np.delete(submatrix, (i, i + 1)), axis=0)
            submatrix = np.delete(submatrix, (j, j + 1)), axis=1)
            # Check if the sum of all elements in the submatrix is equal to 19
            if np.sum(submatrix) == 19:
                # If it is, add the submatrix to the list of submatrices
                submatrices.append(submatrix)
    # Return the list of submatrices that have a sum of all elements equal to 19
    return submatrices
