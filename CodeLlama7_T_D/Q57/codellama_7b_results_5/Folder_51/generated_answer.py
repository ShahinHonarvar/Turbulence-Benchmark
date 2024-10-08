
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary submatrix with the current row and column
            temp_submatrix = matrix[i:i+1, j:j+1]

            # Check if the sum of all integers in the temporary submatrix is equal to -46
            if np.sum(temp_submatrix) == -46:
                # If it is, add the temporary submatrix to the list of submatrices
                submatrices.append(temp_submatrix)

    # Return the list of all submatrices that have a sum of all integers equal to -46
    return submatrices
