
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape

    for x in range(rows):
        for y in range(cols):
            sub_matrices = [matrix[i:i+x+1,j:j+y+1] for i in range(rows-x) for j in range(cols-y)]
            for sub_matrix in sub_matrices:
                if sub_matrix.size == 43:
                    count += 1
    return count
