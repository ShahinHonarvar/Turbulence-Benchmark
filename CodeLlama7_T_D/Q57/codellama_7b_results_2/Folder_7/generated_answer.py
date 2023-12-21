
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices
    submatrices = []

    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a list to store the elements of the submatrix
            submatrix = []

            # Add the elements of the submatrix to the list
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    if k < matrix.shape[0] and l < matrix.shape[1]:
                        submatrix.append(matrix[k][l]])

            # Check if the sum of all elements in the submatrix is equal to -128
            if np.sum(submatrix) == -128:
                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    return submatrices
