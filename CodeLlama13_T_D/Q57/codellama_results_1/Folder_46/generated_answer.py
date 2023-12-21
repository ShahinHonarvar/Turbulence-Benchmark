
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the sum of elements in the submatrix
            temp_sum = 0

            # Loop over each element in the submatrix
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    # Add the current element to the temporary sum
                    temp_sum += matrix[k][l]

                    # If the temporary sum is equal to 416, add the submatrix to the result list
                    if temp_sum == 416:
                        result.append(matrix[i:k+1, j:l+1])

    # Return the result list
    return result
