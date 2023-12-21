
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Check if the matrix is empty
    if not matrix:
        return []

    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop over each row of the matrix
    for i in range(len(matrix)):
        # Loop over each column of the matrix
        for j in range(len(matrix[i])):
            # Initialize an empty list to store the elements of the submatrix
            submatrix_elements = []

            # Loop over each element of the submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    if row < len(matrix) and col < len(matrix[row]):
                        submatrix_elements.append(matrix[row][col])

            # Check if the sum of the elements in the submatrix is -452
            if sum(submatrix_elements) == -452:
                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix_elements)

    # Return the list of all submatrices that have a sum of -452
    return submatrices
