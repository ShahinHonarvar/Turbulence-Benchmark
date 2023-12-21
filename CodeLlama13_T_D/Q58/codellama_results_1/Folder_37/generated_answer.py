
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize a count variable to 0
    count = 0
    
    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the current row
        for j in range(len(matrix[i])):
            # Check if the current element is equal to n
            if matrix[i][j] == n:
                # If it is, increment the count variable
                count += 1
    
    # Return the final count
    return count
