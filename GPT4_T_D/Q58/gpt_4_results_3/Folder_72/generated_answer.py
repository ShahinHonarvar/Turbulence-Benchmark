
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, columns = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(columns):
            for k in range(i+1, rows+1, 1):
                for l in range(j+1, columns+1, 1):
                    if (k - i) * (l - j) == 16:
                        count += 1
    return count
