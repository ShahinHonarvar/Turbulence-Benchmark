
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop over each row in the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column in the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the elements in the submatrix
            submatrix_sum = 0

            # Loop over each element in the submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    # Add the element to the sum of the elements in the submatrix
                    submatrix_sum += matrix[row][col]

            # Check if the sum of the elements in the submatrix is equal to -63
            if submatrix_sum == -63:
                # If the sum is equal to -63, add the submatrix to the list of submatrices
                submatrices.append(matrix[i:i + 3][j:j + 3]])

    # Return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -63. If no such submatrix is found, return an empty list.
    return submatrices
