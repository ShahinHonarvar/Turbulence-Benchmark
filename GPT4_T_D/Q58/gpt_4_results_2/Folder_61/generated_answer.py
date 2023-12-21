
import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.size<4:
        return 0
    rows,cols = matrix.shape
    count = 0
    for row in range(rows-1):
        for col in range(cols-1):
            submatrix = matrix[row:row+2, col:col+2]
            if submatrix.size == 4:
                count+=1
    return count
