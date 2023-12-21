
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the elements of the current submatrix
            temp = []
            
            # Iterate over each row of the submatrix
            for k in range(i, matrix.shape[0]):
                # Iterate over each column of the submatrix
                for l in range(j, matrix.shape[1]):
                    # Add the element at position (k, l) to the temporary list
                    temp.append(matrix[k][l])
            
            # Check if the sum of all elements in the temporary list is equal to -137
            if np.sum(temp) == -137:
                # If it is, add the submatrix to the result list
                result.append(np.array(temp).reshape((len(temp), 1)))
    
    # Return the result list
    return result
