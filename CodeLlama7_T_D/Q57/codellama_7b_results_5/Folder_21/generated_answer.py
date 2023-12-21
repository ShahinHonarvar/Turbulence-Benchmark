
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the submatrix
            submatrix_sum = 0

            # Calculate the sum of all integers in the submatrix
            for row in range(i, i + 2):
                for col in range(j, j + 2):
                    submatrix_sum += matrix[row][col]

            # If the sum is equal to -936, add the submatrix to the result list
            if submatrix_sum == -936:
                result.append(matrix[i:i + 2, j:j + 2])

    # Return the result list
    return result
