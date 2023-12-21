
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows-1):
        for j in range(cols-1):
            if i+1 < rows and j+1 < cols:
                sub_matrix = matrix[i:i+2, j:j+2]
                if sub_matrix.size == 8:
                    count += 1
    return count
