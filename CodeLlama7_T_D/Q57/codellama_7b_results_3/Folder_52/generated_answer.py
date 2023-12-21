
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop over each row in the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column in the matrix
        for j in range(matrix.shape[1]):
            # Initialize a counter for the sum of integers in the submatrix
            sum = 0

            # Loop over each element in the submatrix
            for row in range(i, i + 2):
                for col in range(j, j + 2):
                    # Add the current element to the sum
                    sum += matrix[row][col]

                    # Check if the sum is equal to 100
                    if sum == 100:
                        # If it is, add the submatrix to the list of submatrices
                        submatrices.append([row - i, col - j])

                        # Break out of the inner loop since we've found a submatrix with the desired sum
                        break

            # Break out of the outer loop since we've found a row with a submatrix with the desired sum
            break

    # Return the list of all submatrices with the desired sum
    return submatrices
