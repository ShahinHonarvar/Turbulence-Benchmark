
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the found submatrices
    found_submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to -157
            if matrix[i,j] == -157:
                # If so, check if the submatrix starting from this element and having the same number of rows and columns as the original matrix is a submatrix with the required sum
                if np.sum(matrix[i:i+matrix.shape[0], j:j+matrix.shape[1]]) == -157:
                    # If so, add it to the list of found submatrices
                    found_submatrices.append(matrix[i:i+matrix.shape[0], j:j+matrix.shape[1]])
    
    return found_submatrices
