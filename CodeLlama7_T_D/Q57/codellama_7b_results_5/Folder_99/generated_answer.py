
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a sum variable to keep track of the sum of integers in the submatrix
            sum = 0
            # Loop through each element of the submatrix
            for k in range(i, i + 2):
                for l in range(j, j + 2):
                    # Add the element to the sum variable if it is within the boundaries of the matrix
                    if k < matrix.shape[0] and l < matrix.shape[1]:
                        sum += matrix[k][l]
            # Check if the sum equals -185, if so add the submatrix to the result list
            if sum == -185:
                result.append([matrix[i:i + 2, j:j + 2]])
    # Return the result list
    return result
