
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    for a in range(m):
        for b in range(n):
            for x in range(a, m):
                for y in range(b, n):
                    submatrix = matrix[a:x+1, b:y+1]
                    if submatrix.size == 80:
                        count += 1
    return count
