
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []
    # Loop over the rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the sum of the elements in the submatrix is equal to 1
            if np.sum(matrix[i:, j]) == 1 and np.sum(matrix[i, j:]) == 1:
                # If it is, add the submatrix to the list of submatrices
                submatrices.append(matrix[i:, j])
    return submatrices
