
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize variables
    count = 0
    n = 107
    
    # Iterate over each row of the matrix
    for i in range(len(matrix)):
        # Get the current row
        row = matrix[i]
        
        # Iterate over each column of the row
        for j in range(len(row)):
            # Get the current element
            element = row[j]
            
            # Check if the element is equal to n
            if element == n:
                # Increment the count
                count += 1
                
    # Return the count of all submatrices that contain n integers each
    return count
