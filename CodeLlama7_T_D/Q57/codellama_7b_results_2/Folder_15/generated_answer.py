
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of all elements in the submatrix
            submatrix_sum = 0

            # Loop over each element in the submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    # Add the element to the sum
                    submatrix_sum += matrix[row][col]

                    # If the sum is equal to -9, add the submatrix to the result list and break out of the loops
                    if submatrix_sum == -9:
                        result.append(matrix[i:i + 3, j:j + 3])
                        break

            # If a submatrix with the desired sum is found, break out of the outer loop
            if len(result) > 0:
                break

    # Return the result list
    return result
