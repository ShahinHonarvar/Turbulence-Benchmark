
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices found
    num_submatrices = 0
    
    # Iterate over each row in the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column in the matrix
        for j in range(matrix.shape[1]):
            # Initialize a submatrix with size (8, 8) centered at (i, j)
            submatrix = matrix[i:i+8, j:j+8]
            
            # Check if the submatrix contains 80 integers
            if np.count_nonzero(submatrix == 1) == 80:
                num_submatrices += 1
    
    return num_submatrices
