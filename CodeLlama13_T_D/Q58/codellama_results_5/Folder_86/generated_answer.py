
import numpy as np
def submatrix_with_n_numbers(matrix):
    # Initialize a count variable
    count = 0
    
    # Loop over all rows and columns of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Check if the current element is equal to 138
            if matrix[i][j] == 138:
                # Increment the count variable
                count += 1
                
    # Return the count of submatrices with 138 integers each
    return count
