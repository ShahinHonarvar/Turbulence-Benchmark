
import numpy as np
def submatrices_with_particular_sum(matrix):
    # Calculate the sum of all integers in each row and column
    row_sums = matrix.sum(axis=1)
    col_sums = matrix.sum(axis=0)
    
    # Find all submatrices that have a particular sum by looping through all rows and columns
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Calculate the sum of all integers in this submatrix
            submatrix_sum = row_sums[i] + col_sums[j] - matrix[i, j]
            
            # If the sum is 28, add it to the list of submatrices
            if submatrix_sum == 28:
                submatrices.append((i, j))
    
    return submatrices
