
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Calculate the sum of all integers in the submatrix
            sum = 0
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    if row < matrix.shape[0] and col < matrix.shape[1]:
                        sum += matrix[row][col]
            # If the sum is equal to -3, add the submatrix to the result list
            if sum == -3:
                submatrix = matrix[i:i + 3, j:j + 3]
                result.append(submatrix)
    # Return the result list
    return result
