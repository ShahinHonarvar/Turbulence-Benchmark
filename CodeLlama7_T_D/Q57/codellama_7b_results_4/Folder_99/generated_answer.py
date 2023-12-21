
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize an empty list to store the elements of the submatrix
            submatrix = []

            # Loop through each row of the submatrix
            for k in range(i, matrix.shape[0]):
                # Loop through each column of the submatrix
                for l in range(j, matrix.shape[1]):
                    # Add the element to the list
                    submatrix.append(matrix[k][l])

            # Check if the sum of all elements in the submatrix is -185
            if sum(submatrix) == -185:
                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices
    return submatrices
