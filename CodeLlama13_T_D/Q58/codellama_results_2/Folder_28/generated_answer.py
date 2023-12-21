
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a count variable to 0
    count = 0
    
    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the matrix
        for j in range(len(matrix[0])):
            # Check if the current element is 37
            if matrix[i][j] == 37:
                # If it is, increment the count by 1
                count += 1
    
    # Return the count of submatrices with 37 integers each
    return count
