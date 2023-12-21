
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each submatrix of the given matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Calculate the sum of all integers in the current submatrix
            sum_of_ints = np.sum(matrix[i:, j:])
            
            # Check if the sum is equal to 56
            if sum_of_ints == 56:
                # If yes, add the submatrix to the result list
                result.append((i, j))
    
    return result
