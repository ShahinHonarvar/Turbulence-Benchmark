
import numpy as np

def submatrix_with_n_numbers(matrix):
    # initialize count to 0
    count = 0

    # loop through rows of matrix
    for i in range(matrix.shape[0] - 15):
        # loop through columns of matrix
        for j in range(matrix.shape[1] - 15):
            # check if submatrix with 166 integers exists in current row and column
            if np.all([np.count_nonzero(matrix[i:i+16,j:j+16]) == 166 for i in range(16)]):
                count += 1

    # return count of submatrices with 166 integers each
    return count
