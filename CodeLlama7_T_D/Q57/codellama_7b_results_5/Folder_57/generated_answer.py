
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the output list
    submatrices = []

    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the matrix
        for j in range(len(matrix[i])):
            # Create a list to store the elements of the current submatrix
            submatrix_elements = []

            # Add the elements of the current submatrix to the output list
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    if row < len(matrix) and col < len(matrix[row]):
                        submatrix_elements.append(matrix[row][col])

            # Check if the sum of the elements in the current submatrix equals 13
            if sum(submatrix_elements) == 13:
                # Add the current submatrix to the output list
                submatrices.append(submatrix_elements)

    return submatrices
