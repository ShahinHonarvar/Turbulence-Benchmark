
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the current submatrix
            temp = []
            
            # Add the current element to the temporary list
            temp.append(matrix[i,j])
            
            # Loop through each row below the current row
            for k in range(i+1, matrix.shape[0]):
                # Add the current element to the temporary list
                temp.append(matrix[k,j])
                
                # Check if the sum of all elements in the temporary list is 78
                if np.sum(temp) == 78:
                    # If so, add the submatrix to the list of submatrices
                    submatrices.append(temp)
                    
    return submatrices
