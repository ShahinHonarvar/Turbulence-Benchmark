
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices
    submatrices = []

    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a list to store the elements of the submatrix
            submatrix_elements = []

            # Add the elements of the submatrix to the list
            for row in range(i, i + 2):
                for col in range(j, j + 2):
                    submatrix_elements.append(matrix[row][col])

            # Check if the sum of the elements of the submatrix is equal to 432
            if sum(submatrix_elements) == 432:
                # If it is, add the submatrix to the list of submatrices
                submatrices.append(submatrix_elements)

    # Return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 432. If no such submatrix is found, the function should return an empty list.
    return submatrices
