
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
            # Define the boundaries of the submatrix
            start_row = i
            end_row = i + 1
            start_col = j
            end_col = j + 1
            # Extract the submatrix from the matrix
            submatrix = matrix[start_row:end_row, start_col:end_col]
            # Calculate the sum of the submatrix
            for row in submatrix:
                for element in row:
                    submatrix_sum += element
            # Check if the sum of the submatrix equals 17
            if submatrix_sum == 17:
                # If it does, add the submatrix to the list of submatrices
                submatrices.append(submatrix)
    # Return the list of all submatrices that have a sum of 17
    return submatrices
