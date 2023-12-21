
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for x in range(1, rows - i + 1):
                for y in range(1, cols - j + 1):
                    submatrix = matrix[i:i+x, j:j+y]
                    if submatrix.size == 111:
                        count += 1
    return count
