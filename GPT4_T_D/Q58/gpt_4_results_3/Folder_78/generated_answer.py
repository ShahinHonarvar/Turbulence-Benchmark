
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for row in range(rows):
        for col in range(columns):
            for i in range(row+1, rows+1):
                for j in range(col+1, columns+1):
                    submatrix = matrix[row:i, col:j]
                    if submatrix.size == 91:
                        count += 1
    return count
