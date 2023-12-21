
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Extract a 2D slice of the matrix starting at (i,j) with shape (2,2)
            submatrix = matrix[i:i+2, j:j+2]
            # Calculate the sum of all integers in the submatrix
            submatrix_sum = np.sum(submatrix)
            # If the sum is equal to 432, add the submatrix to the list of submatrices
            if submatrix_sum == 432:
                submatrices.append(submatrix)
    return submatrices
