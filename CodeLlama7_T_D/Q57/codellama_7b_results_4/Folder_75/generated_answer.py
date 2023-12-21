
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the elements in the submatrix
            submatrix_sum = 0
            # Calculate the sum of the elements in the submatrix
            for row in range(i, i + 2):
                for col in range(j, j + 2):
                    submatrix_sum += matrix[row][col]
            # Check if the sum of the elements in the submatrix is equal to 16
            if submatrix_sum == 16:
                # If the sum is equal to 16, add the submatrix to the list of submatrices
                submatrices.append(matrix[i:i + 2, j:j + 2])
    # Return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 16. If no such submatrix is found, the function should return an empty list.
    return submatrices
