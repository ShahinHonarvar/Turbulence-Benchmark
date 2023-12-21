
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    results = []
    
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the current submatrix
            temp = []
            
            # Loop over each row and column of the submatrix
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    # Add the current element to the temporary list
                    temp.append(matrix[k, l])
            
            # Check if the sum of all elements in the submatrix is equal to 3
            if np.sum(temp) == 3:
                # If it is, add the submatrix to the results list
                results.append(np.array(temp))
    
    # Return the results list
    return results
