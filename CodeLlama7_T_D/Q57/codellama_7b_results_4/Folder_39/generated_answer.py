
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
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    # Add the element to the sum of the submatrix
                    submatrix_sum += matrix[row][col]
            # Check if the sum of the submatrix equals 66
            if submatrix_sum == 66:
                # If it does, add the submatrix to the list of submatrices
                submatrices.append(matrix[i:i+3, j:j+3])
    # Return the list of all submatrices that have a sum of 66
    return submatrices
