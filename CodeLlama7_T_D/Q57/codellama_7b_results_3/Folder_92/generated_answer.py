
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the elements in the submatrix
            sum = 0

            # Loop over each element in the submatrix
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    # Calculate the sum of the elements in the submatrix
                    sum += matrix[k][l]

            # Check if the sum of the elements in the submatrix is equal to -3
            if sum == -3:
                # Add the submatrix to the list of submatrices
                submatrices.append(matrix[i:i + 3, j:j + 3])

    # Return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -3. If no such submatrix is found, the function should return an empty list.
    return submatrices
