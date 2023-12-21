
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
            for row_index in range(i, i + 3):
                if row_index < matrix.shape[0]:
                    for col_index in range(j, j + 3):
                        if col_index < matrix.shape[1]:
                            submatrix.append(matrix[row_index][col_index]])

            # Check if the sum of the elements in the submatrix is equal to -137
            if sum(submatrix) == -137:
                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices
    return submatrices
