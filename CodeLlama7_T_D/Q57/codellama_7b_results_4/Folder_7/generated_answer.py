
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices with sum -128
    submatrices = []
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the elements in the submatrix
            submatrix_sum = 0
            # Loop over each element in the submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    # Add the element to the sum of the submatrix
                    submatrix_sum += matrix[row][col]
            # Check if the sum of the elements in the submatrix is equal to -128
            if submatrix_sum == -128:
                # If it is, append the submatrix to the list of submatrices with sum -128
                submatrices.append(matrix[i:i + 3][j:j + 3]])
    # Return the list of submatrices with sum -128
    return submatrices
