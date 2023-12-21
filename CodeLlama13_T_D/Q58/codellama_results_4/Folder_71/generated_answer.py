
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize a counter for the number of submatrices found
    count = 0
    
    # Iterate over each row of the matrix
    for i in range(len(matrix)):
        # Iterate over each column of the matrix
        for j in range(len(matrix[i])):
            # Initialize a temporary matrix to store the submatrix
            temp_matrix = np.zeros((n, n), dtype=int)
            
            # Fill the temporary matrix with the elements of the main matrix
            for k in range(n):
                for l in range(n):
                    temp_matrix[k][l] = matrix[i+k][j+l]
            
            # Check if the temporary matrix contains 78 integers
            if np.count_nonzero(temp_matrix == 78) == n**2:
                count += 1
    
    return count
