
import numpy as np
def submatrix_with_n_numbers(matrix):
    # Initialize a count variable to keep track of the number of submatrices with 23 integers
    count = 0
    
    # Loop through each row and column of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Check if the current element is equal to 23
            if matrix[i][j] == 23:
                # If it is, increment the count by 1 and add the current submatrix to a list of submatrices
                count += 1
                submatrices.append(matrix[i-2:i+3, j-2:j+3])
    
    # Return the count of all submatrices with 23 integers
    return count
