
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    results = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the current submatrix
            temp = []
            
            # Add the current element to the temporary list
            temp.append([matrix[i, j]])
            
            # Loop through each row and column of the submatrix
            for k in range(i + 1, matrix.shape[0]):
                for l in range(j + 1, matrix.shape[1]):
                    # Add the current element to the temporary list
                    temp.append([matrix[k, l]])
            
            # Check if the sum of all elements in the submatrix is equal to -59
            if np.sum(temp) == -59:
                # If it is, add the submatrix to the results list
                results.append(temp)
    
    # Return the results list
    return results
