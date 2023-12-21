
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Convert the matrix into a list of lists for easier manipulation
    matrix = matrix.tolist()
    
    # Initialize an empty list to store the results
    result = []
    
    # Loop through each row in the matrix
    for i in range(len(matrix)):
        # Loop through each column in the matrix
        for j in range(len(matrix[0])):
            # If the sum of all integers in the submatrix starting from (i, j) is -97, append it to the result list
            if np.sum(np.array(matrix[i][j:]) == -97):
                result.append([matrix[i][j:]])
    
    # Return the result list
    return result
