
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with the required sum
    submatrices = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of integers in the current submatrix
            current_sum = 0
            
            # Loop through the rows and columns of the submatrix
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    # Add the integer at the current position to the sum
                    current_sum += matrix[k][l]
            
            # If the sum of integers in the current submatrix is 19, add it to the list of submatrices
            if current_sum == 19:
                submatrices.append(matrix[i:k+1, j:l+1])
    
    # Return the list of submatrices with the required sum
    return submatrices
