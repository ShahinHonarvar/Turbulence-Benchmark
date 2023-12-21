
import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Takes a two-dimensional numpy matrix of integers and returns the count of all
    submatrices that contain 15 integers each. If no such submatrix is found,
    return 0.
    """
    n = 15 # number of integers in each submatrix
    count = 0 # initialize counter
    for i in range(len(matrix) - n + 1): # iterate over rows
        for j in range(len(matrix[i]) - n + 1): # iterate over columns
            submatrix = matrix[i:i+n, j:j+n] # create submatrix
            if np.sum(submatrix) == n * (n + 1) // 2: # check if submatrix contains n integers
                count += 1 # increment counter
    return count # return number of submatrices that contain n integers each
