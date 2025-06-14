
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    results = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary variable to store the sum of the elements in the submatrix
            temp_sum = 0
            
            # Loop through each element in the submatrix
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    # Calculate the sum of the elements in the submatrix
                    temp_sum += matrix[k][l]
            
            # If the sum of the elements in the submatrix is equal to -10, add the submatrix to the results list
            if temp_sum == -10:
                results.append(matrix[i:k+1, j:l+1])
    
    return results
