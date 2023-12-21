
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the found submatrices
    submatrices = []

    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Check if the sum of all integers in the submatrix starting from (i, j) and having a size of 3x3 equals 28
            if np.sum(matrix[i:i+3,j:j+3]) == 28:
                # If yes, add the submatrix to the list of found submatrices
                submatrices.append(matrix[i:i+3,j:j+3])

    return submatrices
