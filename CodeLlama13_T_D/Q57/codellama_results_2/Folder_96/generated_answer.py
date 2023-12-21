
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    
    # Iterate over each submatrix of the given matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Calculate the sum of all integers in the current submatrix
            curr_sum = np.sum(matrix[i:i+3, j:j+3])
            
            # If the sum is equal to -63, add the submatrix to the list
            if curr_sum == -63:
                submatrices.append(matrix[i:i+3, j:j+3].copy())
    
    return submatrices
