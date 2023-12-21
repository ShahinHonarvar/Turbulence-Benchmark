import numpy as np
def submatrix_with_particular_sum(matrix):
    res = []
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            curr = matrix[row][col]
            curr_sum = curr + matrix[row][:col] + matrix[:row][col] + matrix[row+1:][col] + matrix[row][col+1:]
            if curr_sum == -779:
                curr_submatrix = np.array(matrix[row:row+1, col:col+1])
                res.append(curr_submatrix)
    return res
