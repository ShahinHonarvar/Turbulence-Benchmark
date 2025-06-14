
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each submatrix of the given matrix
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Calculate the sum of all integers in the current submatrix
            sum = np.sum(matrix[i:i+2, j:j+2])
            
            # If the sum is equal to 997, add the submatrix to the result list
            if sum == 997:
                result.append((i, j))
    
    return result
