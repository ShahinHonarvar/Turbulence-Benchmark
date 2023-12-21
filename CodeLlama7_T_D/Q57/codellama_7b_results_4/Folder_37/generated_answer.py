
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Create a copy of the current submatrix
            submatrix = matrix[i:, j:].copy()
            # Sum all the integers in the submatrix
            sum_submatrix = np.sum(submatrix)
            # If the sum is equal to -82, add the submatrix to the list of submatrices
            if sum_submatrix == -82:
                submatrices.append(submatrix)
    return submatrices
