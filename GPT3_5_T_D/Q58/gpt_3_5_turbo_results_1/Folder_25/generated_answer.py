
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            for m in range(i, rows):
                for n in range(j, cols):
                    if np.sum(matrix[i:m+1, j:n+1] == 66) == (m-i+1)*(n-j+1):
                        count += 1
    return count
