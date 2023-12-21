
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Create a copy of the original matrix
            submatrix = np.copy(matrix)
            # Remove all elements from the submatrix that are not in the current row and column
            submatrix = submatrix[i:, j:]
            # Check if the sum of all elements in the submatrix is equal to 8
            if submatrix.sum() == 8:
                # If it is, add the submatrix to the list of submatrices
                submatrices.append(submatrix)
    # Return the list of all submatrices that have a sum of 8
    return submatrices
