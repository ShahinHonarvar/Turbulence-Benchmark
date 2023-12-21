
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary submatrix with the current element
            temp_submatrix = np.array([[matrix[i, j]]])
            
            # Check if the sum of all integers in the temporary submatrix is 59
            if np.sum(temp_submatrix) == 59:
                # If so, add the temporary submatrix to the results list
                results.append(temp_submatrix)
                
    return results
