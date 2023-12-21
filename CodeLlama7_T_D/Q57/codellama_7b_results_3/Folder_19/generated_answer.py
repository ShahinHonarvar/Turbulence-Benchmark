
import numpy as np

def submatrix_with_particular_sum(matrix, target_sum):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Calculate the sum of all elements in the submatrix
            submatrix_sum = np.sum(matrix[i:,j]) + np.sum(matrix[i,j+1:]) - matrix[i,j]
            # Check if the sum of all elements in the submatrix is equal to the target sum
            if submatrix_sum == target_sum:
                # If so, add the submatrix to the list of submatrices
                submatrices.append(matrix[i:,j])

    # Return the list of submatrices that have a sum equal to the target sum
    return submatrices
