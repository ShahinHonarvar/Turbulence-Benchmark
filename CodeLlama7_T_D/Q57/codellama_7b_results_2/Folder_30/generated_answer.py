
import numpy as np

def submatrix_with_particular_sum(matrix, sum):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize an empty list to store the elements of the submatrix
            submatrix = []

            # Loop through each row of the submatrix
            for k in range(i, i + 3):
                # Loop through each column of the submatrix
                for l in range(j, j + 3):
                    # Add the element to the list of elements
                    submatrix.append(matrix[k][l]])
            # Check if the sum of the elements in the submatrix is equal to the target sum
            if sum(submatrix) == sum:
                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix)
    return submatrices
