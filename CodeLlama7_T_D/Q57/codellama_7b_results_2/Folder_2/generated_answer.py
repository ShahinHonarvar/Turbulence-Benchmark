
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []
    # Iterate over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Calculate the sum of the elements in the submatrix
            submatrix_sum = np.sum(matrix[i:,j]) + np.sum(matrix[i,j+1:]) - matrix[i,j]
            # Check if the sum is equal to -863
            if submatrix_sum == -863:
                # Add the submatrix to the list of submatrices
                submatrices.append(matrix[i:,j] + matrix[i,j+1:])
    # Return the list of submatrices
    return submatrices
