
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []

    # Loop through each submatrix of the given matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Check if the sum of all integers in the current submatrix equals -13
            if sum(matrix[i][j]) == -13:
                # Add the current submatrix to the result list
                result.append(matrix[i][j])

    # Return the result list
    return result
