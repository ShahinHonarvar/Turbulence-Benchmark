
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    target_sum = 154
    
    m, n = matrix.shape
    
    for i in range(m):
        for j in range(n):
            sub_sum = 0
            for k in range(i, m):
                for l in range(j, n):
                    sub_sum += matrix[k][l]
                    if sub_sum == target_sum:
                        count += 1
    
    return count
