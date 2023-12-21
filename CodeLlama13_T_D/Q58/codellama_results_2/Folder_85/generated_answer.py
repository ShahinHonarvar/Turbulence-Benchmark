
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize a counter for the number of submatrices with 13 integers
    count = 0
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the submatrix
            temp_matrix = np.zeros((n, n), dtype=int)
            
            # Fill the temporary matrix with values from the main matrix
            for k in range(n):
                for l in range(n):
                    temp_matrix[k, l] = matrix[i + k, j + l]
                    
            # Check if the temporary matrix contains 13 integers
            if np.sum(temp_matrix == 1) == n * n:
                count += 1
                
    return count
