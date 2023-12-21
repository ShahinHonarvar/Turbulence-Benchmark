
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Create a 2D array of all possible submatrices
    submatrices = np.lib.stride_tricks.as_strided(matrix, shape=(matrix.shape[0] - 1, matrix.shape[1] - 1), strides=matrix.strides * 2)
    
    # Calculate the sum of all integers in each submatrix
    sums = np.sum(submatrices, axis=(1, 2))
    
    # Return the list of all submatrices with a particular sum
    return [submatrices[i] for i in range(len(sums)) if sums[i] == 830]
