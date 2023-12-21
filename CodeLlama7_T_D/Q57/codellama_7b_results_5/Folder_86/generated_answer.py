
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize an empty list to store the elements of the submatrix
            submatrix = []

            # Add the elements of the submatrix to the list
            for k in range(i, i + 2):
                for l in range(j, j + 2):
                    if (k < matrix.shape[0]) and (l < matrix.shape[1]):
                        submatrix.append(matrix[k][l]])

            # Check if the sum of all elements in the submatrix is -394
            if sum(submatrix) == -394:
                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices
    return submatrices
