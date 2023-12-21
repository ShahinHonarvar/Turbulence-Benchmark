
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with sum -336
    submatrices = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the submatrix elements
            temp = []
            
            # Add the element at (i,j) to the temporary list
            temp.append(matrix[i][j])
            
            # Loop through each row and column after (i,j)
            for k in range(i+1, matrix.shape[0]):
                for l in range(j+1, matrix.shape[1]):
                    # Add the element at (k,l) to the temporary list
                    temp.append(matrix[k][l])
            
            # Check if the sum of all elements in the temporary list is -336
            if sum(temp) == -336:
                # If it is, add the submatrix to the list of submatrices
                submatrices.append(temp)
    
    # Return the list of submatrices with sum -336
    return submatrices
