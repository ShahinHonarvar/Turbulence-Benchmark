
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the submatrix
            submatrix_sum = 0

            # Loop through each element of the submatrix
            for row in range(i, i + 2):
                for col in range(j, j + 2):
                    # Calculate the sum of the elements in the submatrix
                    submatrix_sum += matrix[row][col]

                    # Check if the sum equals -452
                    if submatrix_sum == -452:
                        # If it does, add the submatrix to the list of submatrices
                        submatrices.append(matrix[i:i + 2, j:j + 2])

            # Reset the sum variable for the next iteration
            submatrix_sum = 0

    # Return the list of all submatrices that have a sum of -452
    return submatrices
