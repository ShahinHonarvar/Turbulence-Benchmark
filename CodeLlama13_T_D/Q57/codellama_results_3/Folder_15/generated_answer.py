
import numpy as np

def submatrix_with_particular_sum(mat):
    # Convert the matrix into a 1D array
    mat = np.reshape(mat, (-1,))
    
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over all possible starting indices
    for i in range(len(mat) - 2):
        # Get the current submatrix
        sub = mat[i:i+3]
        
        # Check if the sum of all integers in the submatrix equals -9
        if np.sum(sub) == -9:
            # Add the submatrix to the result list
            result.append(sub)
    
    return result
