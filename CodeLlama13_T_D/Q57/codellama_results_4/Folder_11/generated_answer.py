
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with particular sum
    submatrices = []
    
    # Loop through each submatrix of the given matrix
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Check if the sum of all integers in the current submatrix is equal to 38
            if np.sum(matrix[i:i+2, j:j+2]) == 38:
                # If the sum is equal to 38, add the submatrix to the list of submatrices
                submatrices.append(matrix[i:i+2, j:j+2])
    
    # Return the list of submatrices with particular sum
    return submatrices
