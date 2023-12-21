
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for length in range(rows+1):
        for breadth in range(columns+1):
            for row in range(rows-length+1):
                for col in range(columns-breadth+1):
                    sub_matrix = matrix[row:row+length, col:col+breadth]
                    if sub_matrix.size == 67:
                        count += 1
    return count
