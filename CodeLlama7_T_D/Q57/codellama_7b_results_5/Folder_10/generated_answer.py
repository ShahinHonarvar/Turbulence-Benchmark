
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the submatrix
            submatrix_sum = 0
            # Loop through each element of the submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    # Add the element to the sum of the submatrix
                    submatrix_sum += matrix[row][col]
            # Check if the sum of the submatrix is equal to 56
            if submatrix_sum == 56:
                # If it is, add the submatrix to the list of submatrices
                submatrices.append(matrix[i:i + 3, j:j + 3])
    # Return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 56. If no such submatrix is found, the function should return an empty list.
    return submatrices
