
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over each row of the matrix
    for i in range(len(matrix)):
        # Iterate over each column of the current row
        for j in range(len(matrix[i])):
            # Initialize a temporary list to store the submatrix
            temp = []
            
            # Add the current element and all elements below it in the same column
            temp.append(matrix[i][j])
            for k in range(i+1, len(matrix)):
                temp.append(matrix[k][j])
                
            # If the sum of all elements in the submatrix is equal to -83, add it to the results list
            if np.sum(temp) == -83:
                results.append(temp)
    
    # Return the results list
    return results
