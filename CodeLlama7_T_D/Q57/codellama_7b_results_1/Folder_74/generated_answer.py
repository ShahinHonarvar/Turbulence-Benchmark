
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices with sum equal to 88
    submatrices = []
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the submatrix
            submatrix_sum = 0
            # Initialize variables to keep track of the starting and ending rows and columns of the submatrix
            start_row = i
            end_row = i
            start_col = j
            end_col = j
            # Loop over each element of the submatrix
            for row in range(start_row, end_row + 1):
                for col in range(start_col, end_col + 1):
                    # Add the element to the sum of the submatrix
                    submatrix_sum += matrix[row][col]
            # If the sum of the submatrix is equal to 88, add the submatrix to the list of submatrices with sum equal to 88
            if submatrix_sum == 88:
                submatrices.append(matrix[start_row:end_row + 1, start_col:end_col + 1])
    # Return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 88. If no such submatrix is found, the function should return an empty list.
    return submatrices
