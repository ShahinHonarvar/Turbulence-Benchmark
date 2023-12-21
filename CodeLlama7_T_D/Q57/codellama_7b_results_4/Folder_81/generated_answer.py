
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Calculate the sum of all integers in the submatrix
            submatrix_sum = np.sum(matrix[i:, j])
            # Check if the sum equals -90
            if submatrix_sum == -90:
                # If it does, add the submatrix to the list
                submatrices.append(matrix[i:, j])
    # Return the list of all submatrices that satisfy the condition
    return submatrices
