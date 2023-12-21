
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the found submatrices
    found_submatrices = []
    
    # Iterate over each submatrix of the given matrix
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Calculate the sum of all integers in the current submatrix
            current_sum = np.sum(matrix[i:i+2, j:j+2])
            
            # If the current sum is equal to -452, add the submatrix to the list of found submatrices
            if current_sum == -452:
                found_submatrices.append(matrix[i:i+2, j:j+2])
    
    # Return the list of found submatrices
    return found_submatrices
