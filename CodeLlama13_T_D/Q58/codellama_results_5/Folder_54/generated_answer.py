
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices with 27 integers
    count = 0
    
    # Iterate over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the submatrix
            temp_matrix = np.zeros((3, 3), dtype=int)
            
            # Populate the temporary matrix with the current row and column indices
            for k in range(3):
                for l in range(3):
                    temp_matrix[k, l] = matrix[i + k, j + l]
                    
            # Check if the temporary matrix contains 27 integers
            if np.count_nonzero(temp_matrix) == 27:
                count += 1
    
    return count
