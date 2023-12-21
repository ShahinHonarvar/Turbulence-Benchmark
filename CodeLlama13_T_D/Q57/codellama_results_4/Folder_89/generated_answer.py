
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over each row of the matrix
    for i in range(len(matrix)):
        # Iterate over each column of the matrix
        for j in range(len(matrix[0])):
            # Initialize a temporary list to store the submatrix
            temp = []
            
            # Iterate over each row and column of the submatrix
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    # Add the current element to the temporary list
                    temp.append(matrix[k][l])
            
            # If the sum of all elements in the submatrix is 80, add it to the result
            if np.sum(temp) == 80:
                result.append(temp)
    
    return result
