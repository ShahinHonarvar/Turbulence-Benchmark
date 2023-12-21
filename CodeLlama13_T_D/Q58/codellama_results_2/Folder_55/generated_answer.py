
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices with 39 integers
    count = 0
    
    # Iterate over each row in the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column in the matrix
        for j in range(matrix.shape[1]):
            # Initialize a submatrix with size (3, 3) centered at the current cell
            submatrix = matrix[i-1:i+2, j-1:j+2]
            
            # Check if the submatrix contains 39 integers
            if np.count_nonzero(submatrix == 39) == 39:
                count += 1
    
    return count
