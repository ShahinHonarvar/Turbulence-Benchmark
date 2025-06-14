
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with a particular sum
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary variable to store the sum of integers in the current submatrix
            current_sum = 0
            
            # Iterate over each element in the current submatrix
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    # Add the current element to the temporary variable
                    current_sum += matrix[k, l]
            
            # If the sum of integers in the current submatrix is equal to -4, add it to the list of submatrices
            if current_sum == -4:
                submatrices.append((i, j))
    
    return submatrices
