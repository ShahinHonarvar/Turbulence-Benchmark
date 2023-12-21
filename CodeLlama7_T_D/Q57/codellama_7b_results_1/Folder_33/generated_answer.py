
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices
    submatrices = []

    # Loop over each row of the matrix
    for i in range(len(matrix)):
        # Loop over each column of the matrix
        for j in range(len(matrix[i])):
            # Initialize a list to store the elements of the submatrix
            submatrix_elements = []

            # Add all elements of the submatrix to the list
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    if row < len(matrix) and col < len(matrix[row])):
                        submatrix_elements.append(matrix[row][col])

            # Check if the sum of all elements in the submatrix is -811
            if sum(submatrix_elements) == -811:
                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix_elements)

    # Return the list of submatrices
    return submatrices
