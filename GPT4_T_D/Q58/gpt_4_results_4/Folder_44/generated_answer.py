
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row, col = np.shape(matrix)
    for i in range(row):
        for j in range(col):
            for m in range(i+1, row+1):
                for n in range(j+1, col+1):
                    if ((m-i)*(n-j)) == 191:
                        count += 1
    return count
