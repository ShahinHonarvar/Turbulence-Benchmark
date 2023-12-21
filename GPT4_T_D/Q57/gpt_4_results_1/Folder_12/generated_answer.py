
import numpy as np

def submatrix_with_particular_sum(matrix):
    all_submatrices = []
    n , m = matrix.shape
    start_x = 0
    while start_x < n:
        end_x = start_x+1
        while end_x <= n:
            start_y = 0
            while start_y < m:
                end_y = start_y+1
                while end_y <= m:
                    submatrix = matrix[start_x:end_x,start_y:end_y]
                    if np.sum(submatrix) == -83:
                        all_submatrices.append(submatrix)
                    end_y += 1
                start_y += 1
            end_x += 1
        start_x += 1
    return all_submatrices
