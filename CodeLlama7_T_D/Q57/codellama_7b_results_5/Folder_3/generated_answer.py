
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []
    
    # Iterate over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            
            # Find the sum of all integers in the submatrix starting from (i, j)
            submatrix_sum = 0
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    submatrix_sum += matrix[k][l]
            
            # Check if the sum of all integers in the submatrix is equal to 54
            if submatrix_sum == 54:
                
                # If it is, add the submatrix to the result list
                result.append(matrix[i:i + 3][j:j + 3]])
            
    # Return the result list
    return result
