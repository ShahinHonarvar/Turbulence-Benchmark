
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Check if the sum of the elements in the submatrix starting from (i, j) is equal to -936
            if np.sum(matrix[i:,j:]) == -936:
                # If it is, add the submatrix to the list of submatrices
                submatrices.append(matrix[i:,j:])
    
    return submatrices
