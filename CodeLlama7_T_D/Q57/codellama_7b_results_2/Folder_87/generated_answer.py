
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the matrix
        for j in range(len(matrix[0])):
            # Initialize a variable to store the sum of the current submatrix
            current_sum = 0

            # Loop through each element of the current submatrix
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    # Add the current element to the sum
                    current_sum += matrix[k][l]

                    # If the sum is equal to the target sum, add the submatrix to the list of submatrices and break out of the loop
                    if current_sum == 35:
                        submatrices.append(matrix[i:i + 3, j:j + 3])
                        break

            # If any submatrix with a sum equal to the target sum has been found, break out of the loop
            if len(submatrices) > 0:
                break

    # Return the list of submatrices
    return submatrices
