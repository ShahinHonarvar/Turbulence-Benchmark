
import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):  
            for x in range(i, m):
                for y in range(j, n):
                    submatrix = matrix[i: x+1, j: y+1]
                    if submatrix.size == 27:
                        count += 1
    return count
