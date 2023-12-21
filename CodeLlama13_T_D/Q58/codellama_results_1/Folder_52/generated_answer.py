
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize a counter for the number of submatrices found
    count = 0
    
    # Iterate over each row in the matrix
    for i in range(len(matrix)):
        # Iterate over each column in the matrix
        for j in range(len(matrix[i])):
            # Initialize a temporary submatrix to store the current submatrix
            temp_submatrix = np.zeros((n, n), dtype=int)
            
            # Check if the current submatrix is valid
            if i + n <= len(matrix) and j + n <= len(matrix[i]):
                # Copy the current submatrix to the temporary submatrix
                temp_submatrix = matrix[i:i+n, j:j+n].copy()
                
                # Check if the temporary submatrix contains 147 integers
                if np.count_nonzero(temp_submatrix) == n**2:
                    # Increment the counter for the number of submatrices found
                    count += 1
    
    # Return the count of submatrices found
    return count
