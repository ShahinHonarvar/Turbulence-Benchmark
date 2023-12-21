
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices found
    count = 0
    
    # Iterate over each row in the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column in the matrix
        for j in range(matrix.shape[1]):
            # Initialize a submatrix with size (4, 4) centered at (i, j)
            submatrix = np.zeros((4, 4))
            
            # Fill the submatrix with values from the original matrix
            for k in range(4):
                for l in range(4):
                    submatrix[k, l] = matrix[i + k - 1, j + l - 1]
            
            # Check if the submatrix contains 144 integers
            if np.sum(submatrix) == 144:
                count += 1
    
    return count
