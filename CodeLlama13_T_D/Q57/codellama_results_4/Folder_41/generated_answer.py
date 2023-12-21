
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the submatrix
            temp_submatrix = []
            
            # Add the current element to the temporary submatrix
            temp_submatrix.append(matrix[i,j])
            
            # Iterate over each row and column of the matrix starting from the next row and column
            for k in range(i+1, matrix.shape[0]):
                for l in range(j+1, matrix.shape[1]):
                    # Add the current element to the temporary submatrix
                    temp_submatrix.append(matrix[k,l])
            
            # Check if the sum of all integers in the temporary submatrix is equal to -26
            if sum(temp_submatrix) == -26:
                # Add the temporary submatrix to the list of submatrices
                submatrices.append(temp_submatrix)
    
    return submatrices
