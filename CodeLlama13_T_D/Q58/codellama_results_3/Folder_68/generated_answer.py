
import numpy as np
def submatrix_with_n_numbers(matrix):
    # Initialize a count variable to 0
    count = 0
    
    # Iterate over each row of the matrix
    for i in range(len(matrix)):
        # Iterate over each column of the matrix
        for j in range(len(matrix[i])):
            # Initialize a temporary submatrix with size (7, 4)
            temp_submatrix = np.zeros((7, 4))
            
            # Fill the temporary submatrix with values from the main matrix
            for k in range(7):
                for l in range(4):
                    temp_submatrix[k][l] = matrix[i+k][j+l]
            
            # Check if the temporary submatrix contains 74 integers
            if np.count_nonzero(temp_submatrix) == 74:
                count += 1
    
    return count
