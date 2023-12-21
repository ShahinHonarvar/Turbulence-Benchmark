
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices found
    count = 0
    
    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the current row
        for j in range(len(matrix[i])):
            # Check if the current element is equal to 56
            if matrix[i][j] == 56:
                # If it is, increment the counter and search for submatrices starting from this element
                count += 1
                submatrix_with_n_numbers(matrix[i][j:])
    
    return count
