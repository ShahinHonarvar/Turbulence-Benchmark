
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each submatrix of the given matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Calculate the sum of all integers in the current submatrix
            sum_of_ints = np.sum(matrix[i:, j:])
            
            # If the sum is equal to 13, add the submatrix to the result list
            if sum_of_ints == 13:
                result.append(matrix[i:, j:])
    
    return result
