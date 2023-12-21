
import numpy as np
def submatrix_with_n_numbers(matrix, n):
    count = 0
    for i in range(len(matrix) - n + 1):
        for j in range(len(matrix[i]) - n + 1):
            if sum([matrix[x][y] for x in range(i, i + n) for y in range(j, j + n)]) == n * (n + 1) // 2:
                count += 1
    return count
