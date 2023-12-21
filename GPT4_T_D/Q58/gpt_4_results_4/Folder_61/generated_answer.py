
import numpy as np

def submatrix_with_n_numbers(np_matrix):
    count = 0
    rows, columns = np_matrix.shape
    for i in range(rows):
        for j in range(columns):
            if i+1 < rows and j+1 < columns:
                count += 1
                
    return count
