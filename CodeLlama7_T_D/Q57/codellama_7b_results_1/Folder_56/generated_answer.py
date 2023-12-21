
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the submatrix
            submatrix_sum = 0
            # Define the boundaries of the submatrix
            start_row = i - 1
            if start_row < 0:
                start_row = 0
            end_row = i + 2
            if end_row > matrix.shape[0]:
                end_row = matrix.shape[0]
            start_col = j - 1
            if start_col < 0:
                start_col = 0
            end_col = j + 2
            if end_col > matrix.shape[1]:
                end_col = matrix.shape[1]
            # Loop over each element of the submatrix
            for row in range(start_row, end_row):
                for col in range(start_col, end_col):
                    # Add the element to the sum of the submatrix
                    submatrix_sum += matrix[row][col]
            # Check if the sum of the submatrix equals -50
            if submatrix_sum == -50:
                # If it does, add the submatrix to the list of submatrices
                submatrices.append(matrix[start_row:end_row, start_col:end_col])
    # Return the list of submatrices that have a sum of -50
    return submatrices
