
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            for size_row in range(1, matrix.shape[0] - row + 1):
                for size_col in range(1, matrix.shape[1] - col + 1):
                    if size_row*size_col == 15:
                        count += 1
    
    return count
