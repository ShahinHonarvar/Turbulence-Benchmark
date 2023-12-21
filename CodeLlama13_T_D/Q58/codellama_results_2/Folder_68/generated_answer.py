
import numpy as np
def submatrix_with_n_numbers(matrix, n):
    # initialize the count of submatrices with 0
    count = 0
    
    # iterate over all possible submatrices
    for i in range(matrix.shape[0] - n + 1):
        for j in range(matrix.shape[1] - n + 1):
            # check if the current submatrix has exactly n numbers
            sub = matrix[i:i+n, j:j+n]
            if np.count_nonzero(sub == n) == n**2:
                count += 1
    
    return count
