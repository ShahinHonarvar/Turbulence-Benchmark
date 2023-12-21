
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    results = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a submatrix with size 3x3
            submatrix = np.zeros((3, 3))
            
            # Fill the submatrix with values from the original matrix
            for k in range(3):
                for l in range(3):
                    submatrix[k][l] = matrix[i+k-1][j+l-1]
            
            # Check if the sum of all integers in the submatrix is 245
            if np.sum(submatrix) == 245:
                # If it is, add the submatrix to the results list
                results.append(submatrix)
    
    # Return the results list
    return results
