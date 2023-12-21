
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a submatrix with size (i, j)
            submatrix = np.zeros((i, j))
            
            # Fill the submatrix with the values from the given matrix
            for k in range(i):
                for l in range(j):
                    submatrix[k, l] = matrix[k + i - 1, l + j - 1]
            
            # Check if the sum of all integers in the submatrix is equal to 28
            if np.sum(submatrix) == 28:
                # If it is, add the submatrix to the results list
                result.append(submatrix)
    
    # Return the results list
    return result
