
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the results
    results = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the current submatrix
            temp = []
            
            # Add the current element to the temporary list
            temp.append(matrix[i, j])
            
            # Iterate over each element below and to the right of the current element
            for k in range(i+1, matrix.shape[0]):
                for l in range(j+1, matrix.shape[1]):
                    # Add the current element to the temporary list
                    temp.append(matrix[k, l])
            
            # Check if the sum of all integers in the current submatrix is equal to 862
            if sum(temp) == 862:
                # If it is, add the submatrix to the results list
                results.append(np.array(temp).reshape((len(temp),1)))
    
    return results
