
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices with sum -43
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
                    # Add the element to the submatrix sum
                    submatrix_sum += matrix[row][col]
            # Check if the submatrix sum is equal to -43
            if submatrix_sum == -43:
                # Add the submatrix to the list of submatrices with sum -43
                submatrices.append(submatrix_sum)
    # Return the list of submatrices with sum -43
    return submatrices
