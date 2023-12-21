import numpy as np
def submatrix_with_n_numbers(matrix):
    res = 0
    for row in range(len(matrix)):
        for col in range(row+1, len(matrix[row])+1):
            cnt = 0
            for k in range(row, col+1):
                cnt += matrix[row][k]
            cnt -= matrix[row][col]
            cnt += matrix[row][col+1]
            cnt -= matrix[k+1][col]
            cnt += matrix[k+1][col+1]
            if cnt == 139:
                res += 1
    return res
