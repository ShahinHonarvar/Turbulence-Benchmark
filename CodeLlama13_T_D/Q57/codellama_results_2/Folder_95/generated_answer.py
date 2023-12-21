
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the found submatrices
    submatrices = []

    # Iterate over all possible rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current element is 19
            if matrix[i, j] == 19:
                # If it is, add the submatrix to the list of found submatrices
                submatrices.append(matrix[i:j+1])

    return submatrices
