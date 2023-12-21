import numpy as np
def submatrix_with_n_numbers(matrix):
    m, n = len(matrix), len(matrix[0])
    if m * n < 80:
        return 0
    count = 0
    for i in range(m):
        for j in range(n):
            count += 1
            if count > 80:
                break
    return count
