
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with sum -25
    submatrices = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the submatrix
            temp = []
            
            # Loop through each row and column of the submatrix
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    # Add the current element to the temporary list
                    temp.append(matrix[k][l])
            
            # Check if the sum of all elements in the submatrix is equal to -25
            if sum(temp) == -25:
                # If so, add the submatrix to the list of submatrices
                submatrices.append(np.array(temp))
    
    # Return the list of submatrices with sum -25
    return submatrices
