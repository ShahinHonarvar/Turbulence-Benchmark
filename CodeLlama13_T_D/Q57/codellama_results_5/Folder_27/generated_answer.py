
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []
    
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the submatrix
            temp = []
            
            # Loop over each element in the submatrix
            for k in range(i, matrix.shape[0] - i):
                for l in range(j, matrix.shape[1] - j):
                    # Add the current element to the temporary list
                    temp.append(matrix[k][l])
            
            # Check if the sum of all elements in the submatrix is equal to 77
            if sum(temp) == 77:
                # If so, add the submatrix to the results list
                result.append(temp)
    
    # Return the results list
    return result
