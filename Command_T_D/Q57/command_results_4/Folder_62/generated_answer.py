import numpy as np
def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            curr_sum = 0
            curr_submatrix = np.array(matrix[i])
            curr_submatrix[j] += 1
            curr_sum += curr_submatrix.sum()
            if curr_sum == 394:
                submatrices.append(curr_submatrix)
    return submatrices
