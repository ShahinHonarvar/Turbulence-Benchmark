
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices found
    count = 0
    
    # Loop through each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 38
            if matrix[i, j] == 38:
                # If it is, check if there are at least 38 elements in a submatrix starting from this element
                for k in range(i, i + 38):
                    for l in range(j, j + 38):
                        if matrix[k, l] == 38:
                            count += 1
    
    # Return the number of submatrices found
    return count
