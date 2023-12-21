
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices with sum equal to 93
    submatrices = []
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of elements in the submatrix
            submatrix_sum = 0
            # Loop over each element in the submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    # Add the element to the sum
                    submatrix_sum += matrix[row][col]
            # Check if the sum of elements in the submatrix is equal to 93
            if submatrix_sum == 93:
                # Add the submatrix to the list of submatrices with sum equal to 93
                submatrices.append(matrix[i:i + 3, j:j + 3])
    return submatrices
