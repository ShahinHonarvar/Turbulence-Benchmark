
import numpy as np

def submatrix_with_particular_sum(matrix, sum):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Create a copy of the original matrix without the current row and column
            submatrix = np.copy(matrix)
            del submatrix[i, :]
            del submatrix[:, j]
            # Check if the sum of all integers in the submatrix is equal to -57
            if np.sum(submatrix) == sum:
                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix)
    return submatrices
