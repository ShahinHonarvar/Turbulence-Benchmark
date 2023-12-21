
import numpy as np
def submatrix_with_n_numbers(matrix):
    # Initialize a count variable to keep track of the number of submatrices found
    count = 0
    
    # Iterate over each row and column of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Check if the current element is equal to 185
            if matrix[i][j] == 185:
                # If it is, increment the count variable
                count += 1
    
    # Return the count of submatrices found
    return count
