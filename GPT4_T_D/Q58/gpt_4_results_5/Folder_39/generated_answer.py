
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for wr in range(r, rows):
                for wc in range(c, cols):
                    sub_matrix = matrix[r:wr+1,c:wc+1]
                    if sub_matrix.size == 59:
                        count += 1
    return count
