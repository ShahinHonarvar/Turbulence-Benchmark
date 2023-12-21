
import numpy as np

def submatrix_with_particular_sum(matrix, sum):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop over all rows and columns of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Check if the current element is equal to the desired sum
            if matrix[i][j] == sum:
                # If it is, add the submatrix to the list of submatrices
                submatrices.append(matrix[i][j])
    return submatrices
